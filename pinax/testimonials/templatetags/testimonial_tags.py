from django import template

from ..models import Testimonial


register = template.Library()


@register.assignment_tag
def random_testimonials(number):
    return Testimonial.objects.filter(active=True).order_by("?")[:number]


@register.assignment_tag
def random_testimonial():
    return Testimonial.objects.filter(active=True).order_by("?")[:1]


@register.assignment_tag
def testimonials(number=None):
    if number is None:
        return Testimonial.objects.filter(active=True).order_by("-added")
    else:
        return Testimonial.objects.filter(active=True).order_by("-added")[:number]
