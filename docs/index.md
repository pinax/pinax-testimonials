# pinax-testimonials


!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.
    
    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-testimonials

Add `pinax-testimonials` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.testimonials",
        # ...
    )

## Usage

In your template where you want to display testimonials there are three ways you
can use template tags to add active testimonials to your page:

    {% load testimonial_tags %}


For random testimonials:

    {% random_testimonials <number> as quotes %}


For testimonials ordered by the date they were added:

    {% testimonials <number> as quotes %}


If you just want a single random testimonial you can use:

    {% random_testimonial as quote %}


To add and manage quotes, you simply add them through the Django admin.
