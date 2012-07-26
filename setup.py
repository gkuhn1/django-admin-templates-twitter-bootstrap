#!/usr/bin/env python

from setuptools import setup, find_packages

template_dirs = [
    'templates/admin/auth/user/*.html',
    'templates/admin/edit_inline/*.html',
    'templates/admin/includes/*.html',
    'templates/admin/*.html',
    'templates/registration/*.html',
]

setup(name='admin_bootstrap',
      version='0.1',
      description='Provides a Twitter bootstrap based interface for django admin.',
      author='Guilherme Kuhn',
      author_email='g.kuhn0@gmail.com',
      url='https://github.com/gkuhn1/django-admin-templates-twitter-bootstrap',
      packages=find_packages(),
      license='GPL',
      package_data={ 'admin_bootstrap': template_dirs },
      include_package_data=True,
     )
