from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pmdc',
    version='0.1.0',
    description='Package metadata compiler: keep calm and use YAML for describe your packages.',
    long_description=long_description,
    url='https://github.com/octolab/pmc',
    author='Kamil Samigullin',
    author_email='kamil@samigullin.info',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords='yaml converter composer npm pip',
    py_modules=['pmc'],
    install_requires=[
        'Click >= 6.6',
        'Jinja2 >= 2.8',
        'PyYAML >= 2.8',
        'requests >= 2.10',
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'pmc=pmc:cli',
        ]
    }
)
