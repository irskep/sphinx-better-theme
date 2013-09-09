Anticipatory FAQ
================

This material will probably move to a blog post at some point.

What's the two-second pitch?
----------------------------

It looks nice, it's easy to style with CSS, and it organizes the layout better.

Better how?
-----------

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
4. Better customization. The default theme teases you by putting some color
   settings in the theme configuration, but a few key components like code
   blocks aren't customizable at all. ``sphinx-better-theme`` makes it easy to
   change settings with little overhead by letting you add your own CSS files
   without all the trouble of making a new theme.

A future version of this theme will have semantic markup.  The default theme
is a sea of ``<div>`` tags. Even if the much-heralded machine-readable web
never pans out, it strikes me as a nice symmetry to have a program's
documentation be easily consumable by other programs. It can also make CSS
rules clearer.

Why encourage customization?
----------------------------

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
--------------------------------------------------------------------

It's much easier to add your own CSS. The theme's CSS rules and markup are a
little easier to understand, and that situation should improve over time.
Additionally, there are more meaningful theme options for disabling
unnecessary widgets.

Why not just contribute to Sphinx itself?
-----------------------------------------

I'll probably make an attempt eventually. For now I'd just like to validate my
ideas.
