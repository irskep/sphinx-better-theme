# -*- coding: utf-8 -*-

extensions = ['sphinx.ext.intersphinx']
templates_path = []
source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx-better-theme'
copyright = u'2013 Steve Johnson'
# The short X.Y version.
version = '0.1.4'
# The full version, including alpha/beta/rc tags.
release = '0.1.4'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

html_theme = 'better'
html_theme_options = {
    'inlinecss': """
    """,
    'cssfiles': ['_static/style.css'],
    'scriptfiles': ['_static/testing.js'],
}
html_theme_path = ['..']
html_title = "{} {}".format(project, release)
html_short_title = "Home"
html_sidebars = {
    '**': ['globaltoc.html'],
    'index': ['globaltoc.html'],
}

html_logo = None
html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_show_sphinx = True
html_show_copyright = True
# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx-better-themedoc'

intersphinx_mapping = {'sphinx': ('http://sphinx-doc.org/', None)}
