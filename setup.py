##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup, find_packages

setup(name='Products.BTreeFolder2',
      version='3.0.1.dev0',
      url='https://github.com/zopefoundation/Products.BTreeFolder2',
      license='ZPL 2.1',
      description="A BTree based implementation for Zope 2's OFS.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=(open('README.rst').read() + '\n' +
                        open('CHANGES.rst').read()),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2 :: Only",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      install_requires=[
          'setuptools',
          'AccessControl',
          'Acquisition',
          'BTrees',
          'ExtensionClass>=4.1a1',
          'Persistence',
          'Zope2 >= 2.13.0a1',
          'zope.container',
          'zope.event',
          'zope.lifecycleevent',
      ],
      include_package_data=True,
      zip_safe=False,
      )
