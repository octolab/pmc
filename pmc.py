import click
import json
import sys
import yaml

sys.tracebacklimit = 0


@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', '--package', type=click.STRING, default='*', help='package name (e.g. composer, npm, etc.)')
@click.option('-o', '--output', type=click.File('wb'), default='-', help='output stream (default stdout)')
@click.argument('filename', type=click.Path(exists=True))
def convert(filename, output, package):
    """ Convert package.meta to package files """
    content = yaml.load(open(filename).read())
    if package == '*':
        output.write(json.dumps(content, indent=2))
        output.flush()
    elif package in content:
        output.write(json.dumps(content[package], indent=2))
        output.flush()
    else:
        click.echo('Package %s not found' % package)


@cli.command()
@click.option('-p', '--package', type=click.STRING, default='*', help='package name (e.g. composer, npm, etc.)')
@click.argument('filename', type=click.Path(exists=True))
def validate(package, filename):
    """ Validate package.meta or its section """
    content = yaml.load(open(filename).read())
    if package == '*':
        click.echo(json.dumps(content, indent=2))
    elif package in content:
        click.echo(json.dumps(content[package], indent=2))
    else:
        click.echo('Package %s not found' % package)
