from django.contrib import admin

# Register your models here.
from landing.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


admin.site.register(User)
