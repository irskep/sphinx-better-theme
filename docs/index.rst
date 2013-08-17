sphinx-better-theme
===================

**sphinx-better-theme** is a theme for Sphinx that tries to be better than the
built-in themes. See the `Anticipatory FAQ`_ for details.

You can get the source and open issues `on Github.`_

.. _on Github.: https://github.com/irskep/sphinx-better-theme

.. toctree::
    :maxdepth: 2

    index.rst
    guide.rst
    demos.rst

Compatibility
-------------

sphinx-better-theme is compatible with Sphinx 0.6.4+ and Jinja 2.3.1+. Older
versions may work but have not been tested.

.. _main_page_reference:

Installation
------------

Method 1: Adding to your source tree
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method is preferred due to the frequency with which sphinx-better-theme is
improved.

1. Put the theme in your source tree. If you use git, you can add
   ``sphinx-better-theme``'s repository as a submodule. Otherwise you can
   `download the zip file`_ and expand it somewhere predictable. Here's an
   example using git::

        > git submodule add \
            https://github.com/irskep/sphinx-better-theme.git \
            docs/sphinx-better-theme
        > git submodule update --init

.. _download the zip file: https://github.com/irskep/sphinx-better-theme/archive/master.zip

2. Add the parent folder of the theme to your :file:`conf.py`. If you use the
   folder structure in the block above, you'd do it like this::

        html_theme_path = ['sphinx-better-theme']

   (because the theme path is ``sphinx-better-theme/better``.)

3. Set ``html_theme`` to ``'better'`` in your :file:`conf.py`.

Method 2: Installing to site-packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If adding the theme to your source tree is impractical for some reason, or if
you need to share it among several repositories, you can install it like a
regular Python package.

1. `Download the zip file.`_

.. _Download the zip file.: https://github.com/irskep/sphinx-better-theme/archive/master.zip

2. Run the usual command::

    > python setup.py install

3. Set ``html_theme_path`` to contain ``better.better_theme_path``, and set
   ``html_theme`` to ``'better'``::

    from better import better_theme_path
    html_theme_path = [better_theme_path]
    html_theme = 'better'

Anticipatory FAQ
----------------

Better how?
^^^^^^^^^^^

The default Sphinx theme isn't bad, and the Python 3 theme is even better. But
both themes are problematic for many projects. Specifically, they are difficult
to customize beyond a few inconsequential color and layout settings. Their
markup and stylesheets do not lend themselves to tweaking. This project aims to
mitigate those problems.

Additionally, ``better-sphinx-theme`` contains a few differences that offer
subjective improvements over the default theme and other built-in themes:

1. Less unnecessary color and fewer different colors. I'm not opposed to the
   use of color on the web. I just think it's more professional to use a
   consistent color palette. This site doesn't use much color, but
   ``better-sphinx-theme`` ought to support color if you want it.
2. Fewer fonts and smaller variations in font styles. Headings don't need to be
   huge to be readable, and the sidebar doesn't always need its own set of
   styles.
3. Forced use of the full page width. `45-90 characters is generally agreed to
   be the most readable line length.
   <http://practicaltypography.com/typography-in-ten-minutes.html>`_ Some
   projects make use of the full width to display tables, but many projects do
   just fine without them.
4. Better customization. The default theme hard-codes several color values that
   would look terrible with different color settings.

A future version of this theme will have semantic markup.  The default theme
is a sea of ``<div>`` tags. Even if the much-heralded machine-readable web
never pans out, it strikes me as a nice symmetry to have a program's
documentation be easily consumable by other programs. It can also make CSS
rules clearer.

Why encourage customization?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Branding is important for even small projects. Take a quick look at `the
built-in Sphinx themes. <http://sphinx-doc.org/theming.html#builtin-themes>`_
They're all pretty distinctive, and several are for specific projects or are
based on themes created for specific projects.

As a maintainer, I don't want my project's documentation to use exactly the
same theme as someone else's. The layout and conventions should be consistent
with other projects in the same environment (in my case, other Python
projects), but it should still be possible to glance at a page and know that
you're looking at Project X, rather than "a project styled using the default
Sphinx template."

A logo helps, but most projects' tiny teams don't have the skills necessary to
create an effective logo. Besides, fonts and colors can have an even stronger
effect on the branding of a site. Just look at `Django's documentation
<https://docs.djangoproject.com/en/1.5/>`_ (which, by the way, uses a custom
Sphinx theme). You can tell at a glance what project's web site you're on. The
same goes for the difference betwen `Python 2's documentation
<http://docs.python.org/2/library/argparse.html>`_ and `Python 3's
documentation. <http://docs.python.org/3.3/library/argparse.html>`_

How does this theme encourage customization better than the default?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. There are more variables to customize.
2. The markup and CSS are easier to understand.
3. The basic look of the theme is subjectively better.

Additionally, a future version of this template will use more granular blocks
for easier overriding of specific parts of the page.

Why not just contribute to Sphinx itself?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I'll probably make an attempt eventually. For now I'd just like to validate my
ideas.

Roadmap
-------

**v0.1:** Basic CSS-customizable style that looks nice in its default state

**v0.2:** Rewrite markup to be semantic and customizable

**v1.0:** Extreme documentation polish and rounding out of edge cases

Other themes to check out
-------------------------

`Cloud <http://pythonhosted.org/cloud_sptheme/cloud_theme.html>`_ is a nice,
feature-rich theme from which I plan to steal more than one feature.
