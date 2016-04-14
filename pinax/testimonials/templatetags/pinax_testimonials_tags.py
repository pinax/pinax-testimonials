from django import template

from ..models import Testimonial


register = template.Library()


@register.assignment_tag
def random_testimonials(number):
    return Testimonial.objects.filter(active=True).order_by("?")[:number]


@register.assignment_tag
def random_testimonial():
    queryset = Testimonial.objects.filter(active=True).order_by("?")
    return queryset[0] if queryset else None


@register.assignment_tag
def testimonials(number=None):
    if number is None:
        return Testimonial.objects.filter(active=True).order_by("-added")
    else:
        return Testimonial.objects.filter(active=True).order_by("-added")[:number]
