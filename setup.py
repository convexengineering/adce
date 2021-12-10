import os, sys
#from setuptools import setup
import distutils.core

from distutils.command.build_py import build_py
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


readme = 'README'

distutils.core.setup(
    name='adce',
    version='1.3.3.2',
    author='Edward Burnell',
    author_email='nburnell@gmail.com',
    description='Fast, transparent first- and second-order automatic differentiation; loving fork of ad by Abraham Lee / tisimst@gmail.com',
    url='http://pythonhosted.org/adce',
    license='BSD License',
    long_description=read(readme),
    package_data={'': [readme]},
    #include_package_data=True,
    packages=['adce', 'adce.admath', 'adce.linalg'],
    keywords=[
        'automatic differentiation',
        'first order',
        'second order',
        'derivative',
        'algorithmic differentiation',
        'computational differentiation',
        'optimization',
        'linear algebra'
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ],
    cmdclass={'build_py': build_py},
    )
