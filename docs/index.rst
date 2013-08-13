Usage
=====

1. Put the theme in your source tree. If you use git, you can add
   ``sphinx-better-theme``'s repository as a submodule::

        > git submodule add \
            https://github.com/irskep/sphinx-better-theme \
            docs/_themes/sphinx-better-theme
        > git submodule update --init

2. Add the parent folder of the theme to your :file:`conf.py`. If you use the
   folder structure in the block above, you'd do it like this::

        html_theme_path = ['_themes/sphinx-better-theme']

3. Set ``html_theme`` to ``'better'`` in your :file:`conf.py`.

.. toctree::
   :maxdepth: 2
