# -*- coding: utf-8 -*-

import sys
from glob import glob
from setuptools import setup, Extension
from distutils.command.build import build


with open('README.md') as f:
    long_description = f.read()

include_dirs = ['src']
libraries = ['speexdsp', 'stdc++']
define_macros = []
extra_compile_args = []

sources = (
    glob('src/noise_suppression.cpp') +
    ['src/speexdsp_ns.i']
)

swig_opts = (
    ['-c++'] +
    ['-I' + h for h in include_dirs]
)


setup(
    name='speexdsp-ns-vulcanlabs',
    version='0.1.3',
    description='Python bindings of speexdsp noise suppression library (Vulcanlabs fork with multi-platform wheels)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lucky Wong, Vulcanlabs',
    author_email='dev@vulcanlabs.co',
    url='https://github.com/hiendang7613vulcan/speexdsp-ns-vulcanlabs',
    packages=['speexdsp_ns'],
    ext_modules=[
        Extension(
            name='speexdsp_ns._speexdsp_ns',
            sources=sources,
            swig_opts=swig_opts,
            include_dirs=include_dirs,
            libraries=libraries,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args
        )
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: C++'
    ],
    license='BSD',
    keywords=['speexdsp_ns', 'noise suppression', 'audio processing', 'speech enhancement'],
    platforms=['Linux', 'MacOS'],
    package_dir={
        'speexdsp_ns': 'src'
    }
)
