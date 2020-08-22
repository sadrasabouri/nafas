# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''Breathing gymnastics application'''


setup(
    name='nafas',
    packages=['nafas'],
    version='0.1',
    description='Breathing gymnastics application',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='info@pycm.ir',
    url='https://github.com/sepandhaghighi/nafas',
    download_url='https://github.com/sepandhaghighi/nafas/tarball/v0.1',
    keywords="python3 python breath breathing meditation",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/nafas',
    },
    install_requires=get_requires(),
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Topic :: Games/Entertainment',
        'Topic :: Utilities',
    ],
    license='MIT',
)