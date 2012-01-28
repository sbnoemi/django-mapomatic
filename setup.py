#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "django-mapomatic",
    version = '0.1',
    author = "Noemi Millman",
    description = "Easy map point management in Django",
    include_package_data = True,
    install_requires = [],
    packages = [
        'mapomatic',
    ],
    scripts = []
)
