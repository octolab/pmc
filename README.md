> # Package metadata compiler
>
> Keep calm and use YAML to describe your packages.

[![Patreon](https://img.shields.io/badge/patreon-donate-orange.svg)](https://www.patreon.com/octolab)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](LICENSE)

## Installation

### Requirements

#### [pip](http://pip.readthedocs.io/en/latest/installing/)

### Optional

#### [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)

### Git (development)

[Fork it before](https://github.com/kamilsk/pmc/fork).

```bash
$ git clone git@github.com:<your github account>/pmc.git
$ cd pmc && composer install
$ git remote add upstream git@github.com:kamilsk/pmc.git
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

## Feedback

[![@kamilsk](https://img.shields.io/badge/author-%40kamilsk-blue.svg)](https://twitter.com/ikamilsk)
[![@octolab](https://img.shields.io/badge/sponsor-%40octolab-blue.svg)](https://twitter.com/octolab_inc)

## Notes

- made with ❤️ by [OctoLab](https://www.octolab.org/)

[![Analytics](https://ga-beacon.appspot.com/UA-109817251-5/pmc/readme)](https://github.com/igrigorik/ga-beacon)
