sphinx-better-theme
===================

**sphinx-better-theme** is a theme for Sphinx that tries to be better than the
built-in themes. See :doc:`anticipatory-faq` for details.

You can get the source and open issues `on Github.`_

.. _on Github.: https://github.com/irskep/sphinx-better-theme

.. toctree::
    :maxdepth: 2

    guide.rst
    demos.rst
    anticipatory-faq.rst

Compatibility
-------------

sphinx-better-theme is compatible with Sphinx 0.6.4+ and Jinja 2.3.1+. Older
versions may work but have not been tested.

.. _main_page_reference:
.. _installation:

Installation
------------

Get it from PyPI::

    > pip install sphinx-better-theme

Or `download the zip file`_ and run the usual command::

    > python setup.py install

.. _download the zip file: https://github.com/irskep/sphinx-better-theme/archive/master.zip

Once the package is installed, make these changes to :file:`conf.py` to direct
Sphinx to use the theme::

    from better import better_theme_path
    html_theme_path = [better_theme_path]
    html_theme = 'better'

Read the Docs Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using sphinx-better-theme with `Read the Docs`_ is easy. You just need to tell
it to install the package.

.. _Read the Docs: https://readthedocs.org/

First, create a :file:`requirements.txt` file just for your docs. It must
contain at least the line ``sphinx-better-theme==0.13``, as well as any other
dependencies your docs might have that are separate from your project's
dependencies. I suggest putting it in your docs folder, e.g. at
:file:`docs/requirements.txt`.

Then, go to your Read the Docs admin panel. Make sure the :guilabel:`Use
virtualenv` checkbox is enabled, and set the :guilabel:`Requirements file`
field to the path to your :file:`requirements.txt` file.

Read the Docs should now build and display your theme correctly, assuming your
:file:`conf.py` contains the changes described above in
:ref:`Installation <installation>`.

Projects using sphinx-better-theme
----------------------------------

* `mrjob <http://mrjob.readthedocs.org/en/latest/>`_ (both narrative and API
  docs)

* `pivotal_tools <http://pythonhosted.org/pivotal_tools/>`_ (single-page
  command line tool documentation)

History/Roadmap
---------------

**v0.1:** Basic CSS-customizable style that looks nice in its default state

**v0.11:** Add easy Google Analytics support

**v0.12:** Improve base styles, responsive layout, document usage with Read the
Docs

**v0.13:** Further style improvements, relbar shows only full titles of
next/previous links

**v0.2:** (planned) Rewrite markup to be semantic and customizable

**v1.0:** (planned) Extreme documentation polish and rounding out of edge cases

Other themes to check out
-------------------------

`Cloud <http://pythonhosted.org/cloud_sptheme/cloud_theme.html>`_ is a nice,
feature-rich theme from which I plan to steal more than one feature.

A few different themes are available for download at
`sphinx-themes. <http://vkvn.github.io/sphinx-themes/>`_

`Read the Docs <https://readthedocs.org/>`_ uses a nice custom theme as the
default for all docs hosted there.

The `Guzzle <http://guzzlephp.org/>`_ project uses a `heavily customized
theme`_ that's also used by `aws-cli <http://aws.amazon.com/cli/>`_.

.. _heavily customized theme: https://github.com/guzzle/guzzle_sphinx_theme
