import sys

import click
from .filesystem import File, Watcher
from .parser import YamlParser
from .processor import Processor


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

    :return: int
    """
    f = File(filename)
    content = YamlParser().parse(f.get_absolute_path())
    for key, processor in Processor.get_registered_processors().iteritems():
        if key in content:
            processed = processor.process(content[key])
            output = sys.stdout if dump else open(f.get_new_name(processor.get_filename()), 'wb')
            output.write(processed)
            output.write("\n")
            output.flush()
    return 0


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def validate(filename):
    """
    Validate package.meta.

    :param str filename:

    :return: int
    """
    f = File(filename)
    content = YamlParser().parse(f.get_absolute_path())
    for key, processor in Processor.get_registered_processors().iteritems():
        if key in content:
            processor.validate(content[key])
    return 0


@cli.command()
@click.option('-d', '--dump', is_flag=True, help='dump to stdout')
@click.argument('filename', type=click.Path(exists=True))
@click.pass_context
def watch(ctx, filename, dump):
    """
    Watch for package.meta changes.

    :param click.Context ctx:
    :param str filename:

    :return: int
    """
    Watcher.watch(filename, lambda: ctx.invoke(convert, filename=filename, dump=dump))
    return 0
