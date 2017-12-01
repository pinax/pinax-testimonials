from django.test import TestCase

from ..models import Testimonial
from ..templatetags.pinax_testimonials_tags import \
    random_testimonial as random_testimonial_tag
from ..templatetags.pinax_testimonials_tags import \
    random_testimonials as random_testimonials_tag
from ..templatetags.pinax_testimonials_tags import \
    testimonials as testimonials_tag


class TestTags(TestCase):

    def setUp(self):
        self.first = Testimonial.objects.create(
            text="first text",
            author="first",
            active=True
        )
        self.second = Testimonial.objects.create(
            text="second text",
            author="second",
            active=True
        )
        # Create an inactive testimonial which should not get returned.
        self.inactive = Testimonial.objects.create(
            text="inactive text",
            author="inactive",
            # active=False  # set False by default
        )
        self.third = Testimonial.objects.create(
            text="third text",
            author="third",
            active=True
        )

    def test_random_testimonials(self):
        """
        Ensure tag returns all active testimonials.
        """
        testimonials = random_testimonials_tag(3)
        self.assertSetEqual(set(testimonials), set([self.first, self.second, self.third]))

    def test_random_testimonial(self):
        """
        Ensure we receive one Testimonial instance.
        """
        testimonial = random_testimonial_tag()
        self.assertTrue(isinstance(testimonial, Testimonial))

    def test_testimonials(self):
        """
        Ensure tag returns all active testimonials in reverse creation order.
        """
        testimonials = testimonials_tag(3)
        self.assertSequenceEqual(testimonials, [self.third, self.second, self.first])
