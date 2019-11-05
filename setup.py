from setuptools import setup, find_packages
import os.path
import re

# reading package's version (same way sqlalchemy does)
with open(
    os.path.join(os.path.dirname(__file__), 'btn_bot', '__init__.py')
) as v_file:
    package_version = \
        re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read())\
        .group(1)


setup(
    name='telegram template bot',
    version=package_version,
    author='Mohamad Khajezade',
    description='An MVC template to develope telegram bot',
    packages=find_packages(),
)
