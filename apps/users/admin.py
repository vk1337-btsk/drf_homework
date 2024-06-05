from django.contrib import admin

from apps.users.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('email',)
