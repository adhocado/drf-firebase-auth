from django.contrib import admin
from .models import FirebaseUser


@admin.register(FirebaseUser)
class FirebaseUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        lambda obj: obj.user.email,
        'uid',
    )
    search_fields = (
        'user__username',
        'user__email',
        'uid',
    )
