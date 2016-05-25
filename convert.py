#!/usr/local/bin/python
import click
import json
import sys
import yaml

sys.tracebacklimit = 0


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-package', '--p', default='*')
def convert(filename, package):
    """ Convert package.meta to presented on it package files """
    content = yaml.load(open(filename).read())
    if package is '*':
        print(json.dumps(content, indent=2))
    elif package in content:
        print(json.dumps(content[package], indent=2))
    else:
        print('Package %s not found' % package)


if __name__ == '__main__':
    convert()
