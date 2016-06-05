from .parser import YamlParser
from .processor import Processor
from os import getcwd, path
import click
import sys


@click.group()
def cli():
    sys.tracebacklimit = 0
    pass


@cli.command()
@click.option('-d', '--dump', is_flag=True, help='dump to stdout')
@click.argument('filename', type=click.Path(exists=True))
def convert(filename, dump):
    """
    Convert package.meta to package file(s).

    :param str filename:
    :param bool dump:

    :return int
    """
    file_abs = filename if path.isabs(filename) else path.join(getcwd(), filename)
    file_dir = path.dirname(file_abs)
    content = YamlParser().parse(file_abs)

    for key, processor in Processor.get_registered_processors().iteritems():
        if key in content:
            processed = processor.process(content[key])
            output = sys.stdout if dump else open(path.join(file_dir, processor.get_filename()), 'wb')
            output.write(processed)
            output.write("\n")
            output.flush()
    return 0


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def validate(filename):
    """
    not implemented yet...

    :param str filename:

    :return int
    """
    click.echo('Not implemented yet.')
    return 0


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def watch(filename):
    """
    not implemented yet...

    :param str filename:

    :return int
    """
    click.echo('Not implemented yet.')
    return 0
