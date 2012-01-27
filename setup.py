# -*- coding: utf-8 -*-
'''
Created on 19.12.2011

@author: cykooz
'''

from setuptools import setup, find_packages

setup(name='testproject',
    version='0.1',
    description=u'',
    long_description='',
    keywords='',
    author='Cykooz',
    author_email='saikuz@mail.ru',
    url='',
    package_dir={'': '.'},
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    install_requires=['distribute',
                      'Django',
                      'pysqlite',
                      'South',
                      'PyYAML',
    ],
    entry_points='''
      [paste.app_factory]
      main = testproject.wsgi:application_factory

      ''',
)
