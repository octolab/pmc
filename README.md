> # Package metadata compiler
>
> Keep calm and use YAML to describe your packages.

## [Documentation](https://github.com/octolab/pmc/wiki)

[![Join the chat at https://gitter.im/octolab/pmc](https://badges.gitter.im/octolab/pmc.svg)](https://gitter.im/octolab/pmc?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Example of usages

- [kamilsk/common:package.meta](https://github.com/kamilsk/Common/blob/3.x/package.meta)

## Installation

### Requirements

#### [pip](http://pip.readthedocs.io/en/latest/installing/)

### Optional

#### [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)

### Git (development)

[Fork it before](https://github.com/octolab/pmc/fork).

```bash
$ git clone git@github.com:<your github account>/pmc.git
$ cd pmc && composer install
$ git remote add upstream git@github.com:octolab/pmc.git
$ pip install --editable .
$ pmc --help
Usage: pmc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  convert   Convert package.meta to package file(s).
  validate  Validate package.meta.
  watch     Watch for package.meta changes.
```

#### Mirror

```bash
$ git remote add mirror git@bitbucket.org:kamilsk/pmc.git
```

### Global

```bash
$ pip install pmdc
$ which pmc
$ pmc --help
Usage: pmc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  convert   Convert package.meta to package file(s).
  validate  Validate package.meta.
  watch     Watch for package.meta changes.
```

## Pulse of repository

### [Changelog](CHANGELOG.md)

### Feedback

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/octolab/pmc)
[![@ikamilsk](https://img.shields.io/badge/author-%40ikamilsk-blue.svg)](https://twitter.com/ikamilsk)

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) and [CONDUCT](CONDUCT.md) for details.

## Security

If you discover any security related issues, please email feedback@octolab.org instead of using the issue tracker.

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
