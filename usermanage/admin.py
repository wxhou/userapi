from django.contrib import admin
from .models import Users


# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'idcard', 'address', 'company', 'created_time')
