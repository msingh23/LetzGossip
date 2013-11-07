from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='LetzGossip',
      version=version,
      packages=['gossip'],	 		
      description="This package contains the implemtation of Gossip protocol",
#      long_description=open('README.txt').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='gossip',
      author='Manu Singh',
      author_email='manusingh.infinity@gmail.com',
      url='',
      license='GPL',
      #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["python","python-zmq"],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
