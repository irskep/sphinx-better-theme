sphinx-better-theme
===================

.. note::
    *This project is a work in progress by one person. I take documentation very
    seriously and won't officially "release" anything until I'm satisfied with it.
    You can track my progress by looking at the* `remaining issues on Github
    <https://github.com/irskep/sphinx-better-theme/issues>`_. *–Steve*

Other pages:

.. toctree::
   :maxdepth: 2

   sphinx_demo.rst
   rst_demo.rst

Usage
-----

1. Put the theme in your source tree. If you use git, you can add
   ``sphinx-better-theme``'s repository as a submodule::

        > git submodule add \
            https://github.com/irskep/sphinx-better-theme \
            docs/_themes/sphinx-better-theme
        > git submodule update --init

2. Add the parent folder of the theme to your :file:`conf.py`. If you use the
   folder structure in the block above, you'd do it like this::

        html_theme_path = ['_themes/sphinx-better-theme']

   (because the theme path is ``_themes/sphinx-better-theme/better``.)

3. Set ``html_theme`` to ``'better'`` in your :file:`conf.py`.

I'm waiting until I get a regular release cycle to implement a PyPI-based
installation procedure.

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

**v0.2:** Drop inheritance of ``basic`` theme and rewrite markup

**v1.0:** Extreme documentation polish and rounding out of edge cases
