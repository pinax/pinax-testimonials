from django import template

from ..models import Testimonial

register = template.Library()


@register.simple_tag
def random_testimonials(number):
    return Testimonial.objects.filter(active=True).order_by("?")[:number]


@register.simple_tag
def random_testimonial():
    queryset = Testimonial.objects.filter(active=True).order_by("?")
    return queryset[0] if queryset else None


@register.simple_tag
def testimonials(number):
    return Testimonial.objects.filter(active=True).order_by("-added")[:number]
