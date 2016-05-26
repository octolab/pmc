from setuptools import setup

setup(
    name='pmc',
    version='1.0',
    py_modules=['pmc'],
    include_package_data=True,
    install_requires=[
        'Click >= 6.6',
        'Jinja2 >= 2.8',
        'PyYAML >= 2.8',
        'requests >= 2.10',
    ],
    entry_points={
        'console_scripts': [
            'pmc=pmc:cli',
        ]
    }
)
