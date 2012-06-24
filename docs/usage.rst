.. _usage:

Usage
=====

Using `marturion` is fairly straight forward. You consume quotes through the use
of two different template tags. One that returns a queryset of all testimonials
and one that returns a randomized queryset::

    {% load marturion_tags %}
    
    {% random_testimonials <number> as quotes %}

or::

    {% load marturion_tags %}
    
    {% testimonials <number> as quotes %}


To input quotes, you simply add them through the Django admin.