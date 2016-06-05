"""
    pmc
    ~~~

    Simple package metadata compiler. You can use it with package.meta to describe your composer, npm, etc. packages.

    :copyright: (c) 2013-2016 OctoLab, https://www.octolab.org/ <feedback@octolab.org>
    :license: MIT
"""

from .processor import Processor, ComposerProcessor
from .parser import Parser, YamlParser

__all__ = [
    'Processor', 'ComposerProcessor',
    'Parser', 'YamlParser',
]
__version__ = '1.0-dev1'
