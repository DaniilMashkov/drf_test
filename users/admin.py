from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import CustomUser, _
from django.contrib import admin


@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('phone', 'city', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'phone', 'city', 'is_staff')
    search_fields = ('email', 'phone', 'city')
    ordering = ('email',)
