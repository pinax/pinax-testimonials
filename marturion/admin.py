from django.contrib import admin

from marturion.models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "added", "active"]


admin.site.register(Testimonial, TestimonialAdmin)