# -*- coding: utf-8 -*-
#
# This file is part of python-statsd-client released under the Apache
# License, Version 2.0. See the NOTICE for more information.


from distutils.core import setup

from statsd import __version__


def fread(filename):
    with open(filename) as f:
        return f.read()


def main():
    setup(name='statsd-client',
          description='StatsD client for Python',
          long_description=fread('README.txt'),
          version=__version__,
          license='Apache 2.0',
          author='Gaelen Hadlett',
          author_email='gaelenh@gmail.com',
          url='https://github.com/gaelenh/python-statsd-client',
          py_modules=['statsd'],
          keywords=['statsd', 'graphite', 'stats'],
          classifiers=['License :: OSI Approved :: Apache Software License',
                       'Programming Language :: Python :: 2.6',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 3',
                       'Topic :: System :: Logging',
                       'Operating System :: MacOS :: MacOS X',
                       'Operating System :: POSIX :: Linux',
                       'Operating System :: Unix',
                       'Intended Audience :: Developers'],
         )

if __name__ == '__main__':
    main()
