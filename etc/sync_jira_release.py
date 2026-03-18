#!/usr/bin/env python3
"""
GitHub to Jira Release Sync
Syncs a specific release from viamrobotics/viam-python-sdk to Jira RSDK project

Usage:
    python sync_jira_release.py 0.42.0
    python sync_jira_release.py v0.42.0

Environment Variables Required:
    GITHUB_TOKEN - GitHub personal access token
    JIRA_BASE_URL - Your Jira instance URL (e.g., https://your-domain.atlassian.net)
    JIRA_EMAIL - Your Jira email address
    JIRA_API_TOKEN - Jira API token
"""

import os
import re
import sys

import requests

# Configuration
GITHUB_REPO = "viamrobotics/viam-python-sdk"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = "RSDK"

# Validate environment variables
assert GITHUB_TOKEN and JIRA_BASE_URL and JIRA_EMAIL and JIRA_API_TOKEN, (
    "❌ Missing required environment variables!\n\tRequired: GITHUB_TOKEN, JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN"
)

# Jira auth
jira_auth = (JIRA_EMAIL, JIRA_API_TOKEN)

# GitHub headers
github_headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {GITHUB_TOKEN}", "X-GitHub-Api-Version": "2022-11-28"}


def parse_release_version(version_input):
    """
    Normalize version input to handle both "0.42.0" and "v0.42.0"
    Returns version without 'v' prefix for consistency
    """
    version = version_input.strip()

    # Remove 'v' prefix if present
    if version.startswith("v"):
        version = version[1:]

    # Basic validation - should look like X.Y.Z or X.Y
    if not re.match(r"^\d+\.\d+(\.\d+)?$", version):
        raise ValueError(f"Invalid version format: {version_input}. Expected format: 0.42.0 or v0.42.0")

    return version


def verify_release_exists(version):
    """Verify release exists on GitHub"""
    tag = version if version.startswith("v") else f"v{version}"
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/tags/{tag}"

    response = requests.get(url, headers=github_headers)

    if response.status_code == 200:
        return response.json(), tag
    else:
        raise Exception(f"Release {tag} not found on {GITHUB_REPO}")


def get_tickets_from_release_notes(tag):
    """
    Get Jira tickets directly from GitHub release notes/description
    Much simpler than comparing commits between releases
    """
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/tags/{tag}"
    response = requests.get(url, headers=github_headers)

    if response.status_code != 200:
        raise Exception(f"Could not fetch release notes for {tag}")

    release_data = response.json()

    # Get the release description/body
    body = release_data.get("body", "")

    if not body:
        print(f"⚠️  Warning: Release {tag} has no description/notes")
        return []

    # Extract all RSDK-XXX ticket IDs from the release notes
    pattern = f"{JIRA_PROJECT_KEY}-\\d+"
    tickets = list(set(re.findall(pattern, body, re.IGNORECASE)))

    return tickets


def create_jira_version(github_version):
    """Create version in Jira RSDK project with format 'Python SDK {version}'"""
    # Format as "Python SDK {version}"
    jira_version_name = f"Python SDK {github_version}"

    url = f"{JIRA_BASE_URL}/rest/api/3/version"

    payload = {
        "name": jira_version_name,
        "project": JIRA_PROJECT_KEY,
        "released": False,
        "description": f"Release {github_version} from {GITHUB_REPO}",
    }

    response = requests.post(url, auth=jira_auth, headers={"Content-Type": "application/json"}, json=payload)

    if response.status_code == 201:
        return response.json()
    elif response.status_code == 400:
        # Version exists, fetch it
        search_url = f"{JIRA_BASE_URL}/rest/api/3/project/{JIRA_PROJECT_KEY}/versions"
        versions = requests.get(search_url, auth=jira_auth).json()
        return next((v for v in versions if v["name"] == jira_version_name), None)
    else:
        raise Exception(f"Failed to create version: {response.text}")


def get_ticket_status(ticket_key):
    """Get current status of ticket"""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_key}"
    params = {"fields": "status"}

    response = requests.get(url, auth=jira_auth, params=params)
    if response.status_code == 200:
        return response.json()["fields"]["status"]["name"]
    return None


def set_fix_version_and_close(ticket_key, version_id):
    """
    Step 1: Set fix version while in "Awaiting Release"
    Step 2: Transition ticket to Closed
    """
    # Step 1: Set fix version first
    update_url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_key}"
    update_payload = {"fields": {"fixVersions": [{"id": version_id}]}}

    response = requests.put(update_url, auth=jira_auth, headers={"Content-Type": "application/json"}, json=update_payload)

    if response.status_code != 204:
        print(f"⚠️  Failed to set fix version for {ticket_key}")
        return False

    # Step 2: Get available transitions
    transitions_url = f"{JIRA_BASE_URL}/rest/api/3/issue/{ticket_key}/transitions"
    response = requests.get(transitions_url, auth=jira_auth)

    transitions = response.json().get("transitions", [])
    close_transition = next((t for t in transitions if t["name"].lower() == "closed"), None)

    if not close_transition:
        print(f"⚠️  No 'Closed' transition for {ticket_key}")
        return False

    # Step 3: Transition to Closed
    payload = {"transition": {"id": close_transition["id"]}}

    response = requests.post(transitions_url, auth=jira_auth, headers={"Content-Type": "application/json"}, json=payload)

    return response.status_code == 204


def main(version_input):
    """Main workflow triggered by version input"""
    print(f"📝 Processing: {version_input}\n")

    # 1. Parse and validate version
    try:
        version = parse_release_version(version_input)
        print(f"🔍 Extracted version: {version}")
    except ValueError as e:
        print(f"❌ {e}")
        return

    # 2. Verify release exists on GitHub
    print("🔍 Checking GitHub for release...")
    try:
        release_data, tag = verify_release_exists(version)
        print(f"✅ Found release {tag} on GitHub")
        print(f"   Published: {release_data['published_at'][:10]}")
        print(f"   Author: {release_data['author']['login']}\n")
    except Exception as e:
        print(f"❌ {e}")
        return

    # 3. Create Jira version
    print(f"📦 Creating Jira version: Python SDK {version}")
    jira_version = create_jira_version(version)
    if not jira_version:
        print("❌ Failed to create Jira version")
        return

    version_id = jira_version["id"]
    print(f"✅ Jira version: {jira_version['name']} (ID: {version_id})\n")

    # 4. Extract Jira tickets from release notes
    print("🔍 Extracting Jira tickets from release notes...")
    ticket_keys = get_tickets_from_release_notes(tag)
    print(f"📋 Found {len(ticket_keys)} unique tickets:")
    print(f"   {', '.join(ticket_keys) if ticket_keys else 'None'}\n")

    if not ticket_keys:
        print("⚠️  No Jira tickets found in this release")
        return

    # 5. Process tickets in "Awaiting Release"
    print("🔄 Processing tickets...\n")
    closed_count = 0
    skipped_count = 0

    for ticket_key in ticket_keys:
        status = get_ticket_status(ticket_key)

        if status == "Awaiting Release":
            print(f"   {ticket_key}: {status} → Setting fix version & closing...")
            if set_fix_version_and_close(ticket_key, version_id):
                print(f"   ✅ {ticket_key} closed with fix version Python SDK {version}")
                closed_count += 1
            else:
                print(f"   ❌ Failed to close {ticket_key}")
        else:
            print(f"   ⏭️  {ticket_key}: {status} (skipped)")
            skipped_count += 1

    # 6. Summary
    print(f"\n{'=' * 60}")
    print("🎉 Release sync complete!")
    print(f"   Version: Python SDK {version}")
    print(f"   Tickets closed: {closed_count}")
    print(f"   Tickets skipped: {skipped_count}")
    print(f"   Total tickets: {len(ticket_keys)}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_jira_release.py <version>")
        print("Examples:")
        print("  python sync_jira_release.py 0.42.0")
        print("  python sync_jira_release.py v0.42.0")
        sys.exit(1)

    version_input = sys.argv[1]
    main(version_input)
