from distutils.core import setup
from setuptools import find_packages

setup(name='askfmcrawler',
      version='0.1.5',
      description='Python askfm crawler.',
      author='uehara1414',
      author_email='akiya.noface@gmail.com',
      url='https://github.com/uehara1414/askfmcrawler',
      packages=find_packages(),
      long_description=open('README.md').read(),
      install_requires=[
            'selenium',
      ])
