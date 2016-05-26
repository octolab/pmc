> # Package metadata compiler
>
> Keep calm and use YAML for describe your [composer](https://getcomposer.org), [npm](https://www.npmjs.com)
> or [pip](https://pypi.python.org/pypi) packages.

## Installation

### Requirements

#### [Python](https://www.python.org/downloads/)

#### [pip](http://pip.readthedocs.io/en/latest/installing/)

```bash
$ pip install --editable .
$ pmc --help
Usage: pmc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  convert   Convert package.meta to package files
  validate  Validate package.meta or its section
```

### Optional

#### [virtualenv](https://virtualenv.pypa.io/en/stable/)

```bash
$ [sudo] easy_install virtualenv
# or
$ [sudo] pip install virtualenv
# or
$ sudo apt-get install python-virtualenv
```
