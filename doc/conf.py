# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/pylint/blob/main/CONTRIBUTORS.txt

from __future__ import annotations

import os
import sys
from datetime import datetime

from pylint import __version__
from pylint.__pkginfo__ import numversion

# Pylint documentation build configuration file, created by
# sphinx-quickstart on Thu Apr  4 20:31:25 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath("exts"))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "pylint_features",
    "pylint_extensions",
    "pylint_messages",
    "pylint_options",
    "pylint_changelog",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_reredirects",
    "myst_parser",
]


# Single file redirects are handled in this file and can be done by a pylint
# contributor. We use the following extension:
# https://documatt.gitlab.io/sphinx-reredirects/usage.html
# Directory redirects are handled in ReadTheDoc admin interface and can only be done
# by pylint maintainers at the following URL:
# https://readthedocs.org/dashboard/pylint/redirects/
redirects: dict[str, str] = {
    # "<source>": "<target>"
    "additional_commands/index": "../index.html",
    "development_guide/index": "api/index.html",
    "development_guide/contribute": "../development_guide/contributor_guide/index.html",
    "development_guide/contributor_guide": "contributor_guide/index.html",
    "development_guide/profiling": "../development_guide/contributor_guide/profiling.html",
    "development_guide/tests/index": "../contributor_guide/tests/index.html",
    "development_guide/tests/install": "../contributor_guide/tests/install.html",
    "development_guide/tests/launching_test": "../contributor_guide/tests/launching_test.html",
    # There was a typo in the original file, don't fix.
    "development_guide/tests/writting_test": "../contributor_guide/tests/writing_test.html",
    "development/testing": "tests/index.html",
    "how_tos/custom_checkers": "../development_guide/how_tos/custom_checkers.html",
    "how_tos/index": "../development_guide/how_tos/index.html",
    "how_tos/plugins": "../development_guide/how_tos/plugins.html",
    "how_tos/transform_plugins": "../development_guide/how_tos/transform_plugins.html",
    "intro": "index.html",
    "messages/messages_introduction": "../user_guide/messages/index.html",
    "messages/messages_list": "../user_guide/messages/messages_overview.html",
    "support": "contact.html",
    "technical_reference/c_extensions": "../user_guide/messages/error/no-member.html",
    "technical_reference/extensions": "../user_guide/checkers/extensions.html",
    "technical_reference/checkers": "../development_guide/technical_reference/checkers.html",
    "technical_reference/features": "../user_guide/checkers/features.html",
    "technical_reference/index": "../development_guide/technical_reference/index.html",
    "technical_reference/startup": "../development_guide/technical_reference/startup.html",
    "user_guide/configuration/naming-styles": "../user_guide/messages/convention/invalid-name.html",
    "user_guide/ide_integration/flymake-emacs": "../installation/ide_integration/flymake-emacs.html",
    "user_guide/ide_integration/ide-integration": "../installation/ide_integration/index.html",
    "user_guide/ide-integration": "installation.html",
    "user_guide/ide_integration/textmate": "../installation/ide_integration/textmate.html",
    "user_guide/index": "installation/index.html",
    "user_guide/message-control": "messages/message_control.html",
    "user_guide/options": "configuration/all-options.html",
    "user_guide/output": "usage/output.html",
    "user_guide/pre-commit-integration": "installation/pre-commit-integration.html",
    "user_guide/run": "usage/run.html",
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Pylint"
current_year = datetime.utcnow().year
copyright = f"2003-{current_year}, Logilab, PyCQA and contributors"  # pylint: disable=redefined-builtin

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The short X.Y version.
version = f"{numversion[0]}.{numversion[1]}"
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "data/**"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# Currently we use the default Furo configuration
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

smartquotes = False

# Custom sidebar templates, maps document names to template names.
# Currently we use the default Furo Sidebar
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Pylintdoc"


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "Pylint.tex",
        "Pylint Documentation",
        "Logilab, PyCQA and contributors",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "pylint", "Pylint Documentation", ["Logilab, PyCQA and contributors"], 1)
]

# pylint: disable-next=consider-using-namedtuple-or-dataclass
intersphinx_mapping = {
    "astroid": ("https://pylint.pycqa.org/projects/astroid/en/latest/", None),
    "python": ("https://docs.python.org/3", None),
}

# Prevent label issues due to colliding section names
# through including multiple documents
autosectionlabel_prefix_document = True

linkcheck_ignore = ["https://github.com/PyCQA/pylint/blob/main/pylint/extensions/.*"]


# -- Options for pylint_changelog extension ------------------------------------

pylint_changelog_user = "PyCQA"
pylint_changelog_project = "pylint"
pylint_changelog_token = os.getenv("GITHUB_TOKEN")
pylint_changelog_exclude_labels = [
    "Documentation 📖",
]
