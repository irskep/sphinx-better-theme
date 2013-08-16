A Better Sphinx Theme
=====================

`**Documentation**`_

`**Demo**`_

.. _Documentation: https://sphinx-better-theme.readthedocs.org/en/latest/

.. _Demo: https://sphinx-better-theme.readthedocs.org/en/latest/demos.html

This is a modified version of the Sphinx default theme with the following
goals:

1. Remove frivolous colors, especially hard-coded ones
2. Improve readability by limiting width and using more whitespace
3. Encourage visual customization through CSS, not themeconf
4. Use semantic markup

So far, only goals 1 and 2 have been met. `Open a ticket` if you'd like
something changed.

.. _Open a ticket: https://github.com/irskep/sphinx-better-theme/issues/new

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
            https://github.com/irskep/sphinx-better-theme \
            docs/sphinx-better-theme
        > git submodule update --init

.. _download the zip file: https://github.com/irskep/sphinx-better-theme/archive/master.zip

2. Add the parent folder of the theme to your :file:`conf.py`. If you use the
   folder structure in the block above, you'd do it like this::

        html_theme_path = ['sphinx-better-theme']

   (because the theme path is ``sphinx-better-theme/better``.)

3. Set ``html_theme`` to ``'better'`` in your :file:`conf.py`.

Method 2: Installing to site-package
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
