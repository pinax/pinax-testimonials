# pinax-testimonials

[Pinax](http://pinaxproject.com/pinax/) is an open source ecosystem
of reusable Django apps, themes, and starter project templates.

As a reusable Django app, `pinax-testimonials` provides the ecosystem with
a well tested, documented, and proven solution for any site that needs
to display testimonials.

## Quickstart

Install the development version:

    pip install pinax-testimonials

Add `pinax.testimonials` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.testimonials",
        # ...
    )

## Usage

In your template where you want to display testimonials there are three ways you
can use template tags to add active testimonials to your page:

    {% load pinax_testimonials_tags %}

For random testimonials:

    {% random_testimonials <number> as quotes %}

For testimonials ordered by the date they were added:

    {% testimonials <number> as quotes %}

If you just want a single random testimonial you can use:

    {% random_testimonial as quote %}

To add and manage quotes, you simply add them through the Django admin.
