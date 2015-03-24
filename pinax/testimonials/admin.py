from django.contrib import admin

from .models import Testimonial


def make_active(modeladmin, request, queryset):
    queryset.update(active=True)
make_active.short_description = "Mark as Active"


def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)
make_inactive.short_description = "Mark as Inactive"


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "added", "active"]
    list_filter = ["active", "added"]
    actions = [make_active, make_inactive]


admin.site.register(Testimonial, TestimonialAdmin)
