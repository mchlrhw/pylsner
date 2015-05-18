#!/usr/bin/python3


from distutils.core import setup


config = {
    'name': 'pylsner',
    'description': 'A Gtk/Cairo widget app',
    'url': 'https://github.com/mrmrwat/pylsner.git',
    'version': '0.1',
    'author': 'mrmrwat',
    'author_email': 'mrmrwat@github.com',
    'license': 'MIT',
    'packages': [
        'pylsner',
        'pylsner/plugins/fills',
        'pylsner/plugins/indicators',
        'pylsner/plugins/metrics',
    ],
}


setup(**config)
