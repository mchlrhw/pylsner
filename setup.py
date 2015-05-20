#!/usr/bin/python3


from setuptools import setup


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
        'pylsner/plugins',
    ],
    'data_files': [
        ('etc/pylsner', [
            'etc/pylsner/config.yml',
            'etc/pylsner/widgets.yml',
        ])
    ],
    'zip_safe': False,
    'entry_points': {
        'console_scripts': [
            'pylsner = pylsner.__main__:main',
        ],
    },
}


setup(**config)
