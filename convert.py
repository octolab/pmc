#!/usr/local/bin/python
import click
import json
import sys
import yaml

sys.tracebacklimit = 0


@click.command()
@click.argument('filename')
def convert(filename):
    content = yaml.load(open(filename).read())
    print(json.dumps(content, indent=2))


if __name__ == '__main__':
    convert()
