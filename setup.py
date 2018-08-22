from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cluc',
    version='0.0.1',
    description='Manage your OpenNebula virtual machines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bmwant/cluc',
    author='Misha Behersky',
    author_email='bmwant@gmail.com',

    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: System :: Networking',
        'Topic :: System :: Clustering',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Unix Shell',
    ],

    keywords='xml rpc utils vm',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'attrs>=18.1.0',
        'click>=6.7',
        'oca>=4.15.0a1',
        'PyInquirer>=1.0.2',
    ],

    extras_require={
        'dev': [
            'twine>=1.11.0',
        ],
    },

    entry_points={
        'console_scripts': [
            'cluc=cluc.cli:cli',
        ],
    },

    project_urls={
        'Read a blog': 'https://bmwlog.pp.ua/',
        'Say Thanks!': 'https://gimmebackmyson.herokuapp.com/',
    },
)
