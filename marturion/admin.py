from django.contrib import admin

from marturion.models import Testimoninal


class TestimoninalAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "added", "active"]


admin.site.register(Testimoninal, TestimoninalAdmin)