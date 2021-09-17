from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import MyUser


admin.site.register(MyUser, UserAdmin)
