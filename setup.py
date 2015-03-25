#!/usr/bin/python3


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name': 'pylsner',
    'description': 'A Gtk/Cairo widget app',
    'url': 'https://github.com/mrmrwat/pylsner.git',
    'version': '0.1',
    'author': 'mrmrwat',
    'author_email': 'mrmrwat@github.com',
    'license': 'MIT',
    'packages': ['pylsner'],
}

setup(**config)
