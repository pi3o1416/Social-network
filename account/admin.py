from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'date_of_birth', 'photo']
