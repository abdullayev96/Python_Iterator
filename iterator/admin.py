from django.contrib.admin import ModelAdmin, site
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'plus_ball', 'minus_ball', 'total_point')
    list_filter = ('id','username')
    search_fields = ('username', 'first_name')
    ordering = ('id',)

    readonly_fields = ('total_point',)

    fieldsets = UserAdmin.fieldsets + (
        ('Qo‘shimcha Ma’lumotlar', {'fields': ('plus_ball', 'minus_ball', 'total_point', 'images', 'user_number')}),

    )



admin.site.register(User, CustomUserAdmin)