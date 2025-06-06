# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

[Link to submit](https://viam.atlassian.net/servicedesk/customer/portal/7)

### Fix Bugs

Look through the [Jira tickets](https://viam.atlassian.net/jira/software/c/projects/RSDK/issues/RSDK-10237?filter=allissues&jql=project%20%3D%20%22RSDK%22%20AND%20component%20%3D%20PythonSDK%20AND%20status%20NOT%20IN%20%28%22Awaiting%20Release%22%2C%20Closed%29%0AORDER%20BY%20created%20DESC) for bug ticket types.

### Implement Features

Look through the [Jira tickets](https://viam.atlassian.net/jira/software/c/projects/RSDK/issues/RSDK-10237?filter=allissues&jql=project%20%3D%20%22RSDK%22%20AND%20component%20%3D%20PythonSDK%20AND%20status%20NOT%20IN%20%28%22Awaiting%20Release%22%2C%20Closed%29%0AORDER%20BY%20created%20DESC) for features which are "task" ticket types.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `viam` for local development.

### Prerequisites

We use [`uv`](https://docs.astral.sh/uv/) to manage our environments and dependencies. Make sure you have `uv` installed.

1. Download/clone a copy of `viam` locally.
2. Install `viam` using `make`:

   ```console
   $ make install
   ```

3. Use `git` (or similar) to create a branch for local development and make your changes:

   ```console
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

4. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

- When testing, make sure you use the correct virtual environment by running either `uv run make test` or `source .venv/bin/activate; make test`

5. Commit your changes and open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `viam` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.
