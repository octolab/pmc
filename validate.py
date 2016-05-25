#!/usr/local/bin/python
import click
import json
import sys
import yaml

sys.tracebacklimit = 0


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-package', '--p', default='*')
def validate(filename, package):
    """ Validate package.meta or it's section """
    content = yaml.load(open(filename).read())
    if package is '*':
        print(json.dumps(content, indent=2))
    elif package in content:
        print(json.dumps(content[package], indent=2))
    else:
        print('Package %s not found' % package)


if __name__ == '__main__':
    validate()
