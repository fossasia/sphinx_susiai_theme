from setuptools import setup

setup(
    name = 'sphinx_susiai_theme',
    version = '0.0.1',
    author = 'Balaji R',
    author_email = 'rbalajis25@gmail.com',
    url = 'https://github.com/fossasia/sphinx_susiai_theme',
    license = 'GNU',
    description = 'A Sphinx theme specific to SUSI AI\'s Projects',
    packages = ['sphinx_susiai_theme'],
    include_package_data = True,
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_susiai_theme = sphinx_susiai_theme'
        ],
        'sphinx_themes': [
            'path = sphinx_susiai_theme:get_html_theme_path'
        ],
    },
    install_requires = ['sphinx>=1.3'],
    platforms = 'any',
    classifiers = [
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx :: Theme",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Documentation",
    ],
    long_description = open('README.rst').read(),
)
