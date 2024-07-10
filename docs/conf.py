# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Viam Python SDK"
copyright = "2022-2024, Viam Inc"
author = "Viam Inc"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src"]
autoapi_file_patterns = ["*.pyi", "*.py"]
autoapi_options = [
    "undoc-members",
    "show-inheritance",
    "inherited-members",
    "show-module-summary",
    "special-members",
    "imported-members",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


def skip_member(app, what, name, obj, skip, options) -> bool:
    if "gen.proto" in name:
        return True
    if "proto" in name:
        if "google" in name:
            return True
    should_keep = ["do_command", "get_geometries", "close", "from_robot", "get_resource_name", "get_operation"]
    if obj.inherited and not any(method in name for method in should_keep):
        return True
    if what == "attribute":
        if "_FIELD_NUMBER" in name:
            return True
        if "DESCRIPTOR" in name:
            return True
    if what == "method":
        if "ClearField" in name:
            return True
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_member)


# -- Options for HTML output -------------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "navigation_depth": -1,
}
