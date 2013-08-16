User guide
==========

If you get stuck, you can look for information in Sphinx's documentation for
`using a theme`_, but I've tried to collect all relevant information right
here. `Open a Github issue`_ if something's missing.

This document assumes you've already set up Sphinx and have some docs written.

.. _using a theme: http://sphinx-doc.org/theming.html#using-a-theme
.. _Open a Github issue: https://github.com/irskep/sphinx-better-theme/issues/new

Installation
------------

Put the theme where Sphinx can find it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

That means `download the zip file`_ and expand it somewhere
predictable, or add it to the repository your documentation is in. Here's an
example using git submodules::

    > git submodule add \
        https://github.com/irskep/sphinx-better-theme \
        docs/sphinx-better-theme
    > git submodule update --init

.. _download the zip file: https://github.com/irskep/sphinx-better-theme/archive/master.zip

You can't just specify the path to the theme; instead, you have to specify a
list of directories where sphinx can look for themes by name. This list is
called ``html_theme_path`` in your :file:`conf.py`.

The path to the actual theme is :file:`sphinx-better-theme/better`, so 
you should set ``html_theme_path`` to wherever you put
:file:`sphinx-better-theme`. Relative paths will be relative to
:file:`conf.py`.

You also need to set ``html_theme = "better"``.

For our git example above, you would set::

  html_theme_path = ['sphinx-better-theme']
  html_theme = 'better'

You should now be able to run ``make html`` and see your documentation styled
similarly to this site.

Customization
-------------

sphinx-better-theme is meant to be customized primarily via CSS. There are a
few options that you can set in :file:`conf.py`, but they are either
functionality-related or appear in more than one annoying-to-type selector.

CSS-based customization is currently limited by the inflexibility of the
markup. That situation should improve over time as sphinx-better-theme sheds
more and more of its inheritance from the basic theme.

Feel free to read `the conf.py for this site`_ to get ideas for your own site.
In particular, I'd recommend setting ``html_short_title`` to ``"Home"`` so the
first breadcrumb says "Home" instead of your long project title.

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
  }

Adding static files
^^^^^^^^^^^^^^^^^^^

This is all in the Sphinx docs, but I'm not about to send you all around the
internet just to find it.

#. Configure a static directory::

    html_static_path = ['_static']

#. Put a file in it (e.g. :file:`docs/_static/cat.png`)

#. Use it.

Using CSS files
^^^^^^^^^^^^^^^

#. Add your CSS file as a static file as above.

#. Add the file name (relative to the static directory) to the
   ``html_theme_options['cssfiles']`` list.

You should read `better's CSS files`_ to get an idea of what selectors you
should override. :file:`better_basic.css_t` is my fork of the basic theme's
CSS, and :file:`better.css_t` is the stylistic overrides.

.. _better's CSS files: https://github.com/irskep/sphinx-better-theme/tree/master/better/static

Using Javascript files
^^^^^^^^^^^^^^^^^^^^^^

Not currently supported. `Open a Github issue`_ and plead your case for why in
the world you would want Javascript on your documentation.
