User guide
==========

For installation instructions, see :doc:`installation`.

If you get stuck, you can look for information in Sphinx's documentation for
`using a theme`_, but in theory all the relevant information is collected right
here. `Open a Github issue`_ if something's missing.

This document assumes you've already set up Sphinx and have some docs written.

.. _using a theme: http://sphinx-doc.org/theming.html#using-a-theme
.. _Open a Github issue: https://github.com/irskep/sphinx-better-theme/issues/new

sphinx-better-theme is meant to be customized primarily via CSS. There are a
few options that you can set in :file:`conf.py`, but they are either
functionality-related or appear in more than one annoying-to-type selector.

CSS-based customization is currently limited by the inflexibility of the
markup. That situation should improve over time as sphinx-better-theme sheds
more and more of its inheritance from the basic theme.

Feel free to read `the conf.py for this site`_ to get ideas for your own site.
In particular, consider setting ``html_short_title`` to ``"Home"`` so the first
breadcrumb says "Home" instead of your long project title.

.. _the conf.py for this site: https://raw.github.com/irskep/sphinx-better-theme/master/docs/conf.py

Theme options
^^^^^^^^^^^^^

Unless you're creating your own theme that inherits from sphinx-better-theme,
you're probably setting theme options in :file:`conf.py`. Here are all the
defaults::

  html_theme_options = {
    # show sidebar on the right instead of on the left
    'rightsidebar': False,

    # inline CSS to insert into the page if you're too lazy to make a
    # separate file
    'inlinecss': '',

    # CSS files to include after all other CSS files
    # (refer to by relative path from conf.py directory)
    'cssfiles': [],

    # show a big text header with the value of html_title
    'showheader': True,

    # show the breadcrumbs and index|next|previous links at the top of
    # the page
    'showrelbartop': True,
    # same for bottom of the page
    'showrelbarbottom': True,

    # show search in the sidebar. some of us think Sphinx's search is
    # garbage and just want it to go away.
    'enablesidebarsearch': True,

    # this option was removed in Sphinx 1.2 but I like being able to set it
    # to False and remove more clutter
    'html_show_sourcelink': False,

    # show the self-serving link in the footer
    'linktotheme': True,

    # width of the sidebar. page width is determined by a CSS rule.
    # I prefer to define things in rem because it scales with the
    # global font size rather than pixels or the local font size.
    'sidebarwidth': '15rem',

    # color of all body text
    'textcolor': '#000000',

    # color of all headings (<h1> tags); defaults to the value of
    # textcolor, which is why it's defined here at all.
    'headtextcolor': '',

    # color of text in the footer, including links; defaults to the
    # value of textcolor
    'footertextcolor': '',

    # Google Analytics info
    'ga_ua': '',
    'ga_domain': '',
  }

Adding static files
^^^^^^^^^^^^^^^^^^^

(This is all vanilla Sphinx, but you'll need it for the next section.)

#. Configure a static directory::

    html_static_path = ['_static']

#. Put a file in it (e.g. :file:`docs/_static/cat.png`).

#. Use it.

Using CSS files
^^^^^^^^^^^^^^^

#. Add your CSS file as a static file as above (like
   :file:`docs/_static/style.css`).

#. Add the file name to the ``html_theme_options['cssfiles']`` list in
   :file:`conf.py` (like
   ``html_theme_options['cssfiles'] = ['_static/style.css']``)

You should read `better's CSS files`_ or poke around with your browser's
element inspector to get an idea of what selectors you should override.
:file:`better_basic.css_t` is my fork of the basic theme's CSS, and
:file:`better.css_t` is the stylistic overrides.

.. _better's CSS files: https://github.com/irskep/sphinx-better-theme/tree/master/better/static

Using Javascript files
^^^^^^^^^^^^^^^^^^^^^^

#. Add your Javascript file as a static file as above.

#. Add the file name (relative to the static directory) to the
   ``html_theme_options['scriptfiles']`` list.
