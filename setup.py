from distutils.core import setup

setup(
    name='sphinx-better-theme',
    version='0.1.4',
    author='Steve Johnson',
    author_email='steve@steveasleep.com',
    packages=['better'],
    package_data={
        'better': [
            '*.html',
            '*.conf',
            'static/*.css_t'
        ]
    },
    url='http://github.com/irskep/sphinx-better-theme',
    license='LICENSE',
    description='A nice-looking, customizable Sphinx theme',
    long_description=open('Readme.rst').read(),
)
