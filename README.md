![](http://pinaxproject.com/pinax-design/patches/pinax-testimonials.svg)

# Pinax Testimonials

[![](https://img.shields.io/pypi/v/pinax-testimonials.svg)](https://pypi.python.org/pypi/pinax-testimonials/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-testimonials.svg)](https://circleci.com/gh/pinax/pinax-testimonials)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-testimonials.svg)](https://codecov.io/gh/pinax/pinax-testimonials)
[![](https://img.shields.io/github/contributors/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-testimonials.svg)](https://github.com/pinax/pinax-testimonials/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-testimonials/)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-testimonials

### Overview

`pinax-testimonials` is a well tested, documented, and proven solution
for any site wanting to display testimonials.

Testimonials contain text by an author with an optional organization affiliation.
For display, testimonials are retrieved randomly or most recent first.


#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

To install pinax-testimonials:

    pip install pinax-testimonials

Add `pinax-testimonials` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        "pinax.testimonials",
        ...
    )

### Usage

In your template where you want to display testimonials there are three ways you
can use template tags to add active testimonials to your page.

First, load the template tags:

    {% load pinax_testimonials_tags %}

For random testimonials:

    {% random_testimonials <number> as quotes %}

For testimonials ordered by the date they were added:

    {% testimonials <number> as quotes %}

For show all testimonials by ordered the date:, just remove number parameter, like this:

    {% testimonials as quotes %}

If you just want a single random testimonial you can use:

    {% random_testimonial as quote %}

And there is an example that how you can show the testimonials, you can do something like this:

    {% testimonials  as quotes %}
        {% for quote in quotes %}
        <p class="lead">
            {{quote.text}}
            {{quote.author}}
        </p>
        {% endfor %}

Add and manage testimonial quotes via the Django admin.


## Change Log

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

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).