![](http://pinaxproject.com/pinax-design/patches/pinax-testimonials.svg)

# Pinax Testimonials

[![](https://img.shields.io/pypi/v/pinax-testimonials.svg)](https://pypi.python.org/pypi/pinax-testimonials/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-testimonials.svg)](https://circleci.com/gh/pinax/pinax-testimonials)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-testimonials.svg)](https://codecov.io/gh/pinax/pinax-testimonials)
[![](https://img.shields.io/github/contributors/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
    * [Template Tags](#template-tags)
    * [Displaying Testimonials](#displaying-testimonials)
    * [Managing Testimonials](#managing-testimonials)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-testimonials

### Overview

`pinax-testimonials` is a well tested, documented, and proven solution
for any site wanting to display testimonials.

Testimonials contain text by an author with an optional organization affiliation.
For display, testimonials are retrieved randomly or most recent first.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8 | 3.9
--------------- | --- | --- | --- | ---  
2.2  |  *  |  *  |  *  |  *   
3.1  |  *  |  *  |  *  |  *  
3.2  |  *  |  *  |  *  |  *  


## Documentation

### Installation

To install pinax-testimonials:

```shell
$ pip install pinax-testimonials
```

Add `pinax.testimonials` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # other apps
    "pinax.testimonials",
]
```

### Usage

#### Template Tags

There are several templatetags which return active testimonials.
Assuming pinax-testimonials tags are loaded via `{% load pinax_testimonials_tags %}` in your template,
use the following template tags:

##### `random_testimonial`

Returns a single random testimonial.

```django
{% random_testimonial as quote %}
```

##### `random_testimonials`

Returns testimonials ordered randomly.

```django
{% random_testimonials as quotes %}
```
or

```django
{% random_testimonials <number> as quotes %}
```

Optional `number` indicates how many testimonials to show. If `number` is not specified this tag returns all active testimonials.

##### `testimonials`

Returns testimonials ordered by date added.

```django
{% testimonials as quotes %}
```

or 

```django
{% testimonials <number> as quotes %}
```

Optional `number` indicates how many testimonials to show. If `number` is not specified this tag returns all active testimonials.

#### Displaying Testimonials

```django
{% testimonials as quotes %}
{% for quote in quotes %}
<p class="lead">
    {{quote.text}}
    {{quote.author}}
</p>
{% endfor %}
```

#### Managing Testimonials

Add and manage testimonial quotes via the Django admin console.


## Change Log

### 3.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 2.0.5

* Make `number` parameter optional in `testimonials` templatetag
* Add unit test to verify all active testimonials are returned

### 2.0.4

* Add django>=1.11 to requirements
* Update requirements for Django 2.0
* Update CI config
* Add sorting guidance for 3rd-party app imports
* Improve documentation markup
* Remove doc build support

### 2.0.3

* fix LONG_DESCRIPTION again

### 2.0.2

* fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.1

* Standardize documentation layout
* Drop Django v1.8, v1.10 support

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.9 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 1.0.5

* Update this change log

### 1.0.4

* Documentation updates

### 1.0.3

* Rename templatetags file to match Pinax convention
* Add tests
* Add initial migration
* Update documentation

### 1.0

* Updated template tags to use `assignment_tags`
* Added bulk operations to admin to mark testimonials as active/inactive
* Renamed from `marturian` to `pinax-testimonials` during the donation from Eldarion to Pinax

### 0.2

* Fixed documenation bug
* Added a template tag for fetching a single random quote

### 0.1.4

* Fixed bug introduction with last bug fix.

### 0.1.3

* Fix bug where the random query select would make it hard to use queryset in a template using index accessors.

### 0.1.2

* Fixed a typo in the model name

### 0.1

* initial release


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct


In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
