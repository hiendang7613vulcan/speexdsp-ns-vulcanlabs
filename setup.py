# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from glob import glob
from setuptools import setup, Extension
from distutils.command.build import build


with open('README.md') as f:
    long_description = f.read()


def get_pkg_config(package, option):
    """Get pkg-config values for a package."""
    try:
        result = subprocess.run(
            ['pkg-config', option, package],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


# Base configuration
include_dirs = ['src']
library_dirs = []
libraries = ['speexdsp', 'stdc++']
define_macros = []
extra_compile_args = []
extra_link_args = []

# Try to get paths from pkg-config
pkg_cflags = get_pkg_config('speexdsp', '--cflags')
pkg_libs = get_pkg_config('speexdsp', '--libs')

for flag in pkg_cflags:
    if flag.startswith('-I'):
        include_dirs.append(flag[2:])

for flag in pkg_libs:
    if flag.startswith('-L'):
        library_dirs.append(flag[2:])

# Add common paths
common_include_paths = ['/usr/local/include', '/usr/local/include/speex', '/usr/include', '/usr/include/speex']
common_lib_paths = ['/usr/local/lib', '/usr/local/lib64', '/usr/lib', '/usr/lib64']

for path in common_include_paths:
    if os.path.exists(path) and path not in include_dirs:
        include_dirs.append(path)

for path in common_lib_paths:
    if os.path.exists(path) and path not in library_dirs:
        library_dirs.append(path)

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
            library_dirs=library_dirs,
            libraries=libraries,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args
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
