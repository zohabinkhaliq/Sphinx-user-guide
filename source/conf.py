# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#project = 'userguide'
#copyright = '2024, Zoha Khaliq'
#author = 'Zoha Khaliq'
#release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []

#templates_path = ['_templates']
#exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']


import sphinx_rtd_theme

# Add 'sphinx_rtd_theme' to the extensions list
extensions = []
templates_path=['sphinx_rtd_theme',]
exclude_patterns = []

# Set the HTML theme to 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'

# Optionally, set the path to the RTD theme if it's not in the default location
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
