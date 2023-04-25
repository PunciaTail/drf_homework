from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from user.models import Users

# admin 페이지
class UserAdmin(BaseUserAdmin):
    # admin 리스트에 표시될 필드
    list_display = ["id","email", "is_admin"]
    list_filter = ["is_admin"]
    # admin의 user수정 페이지에서 보여지는 부분
    fieldsets = [
        (None, {"fields": ["password", "gender", "age", "bio"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # admin의 user생성 페이지에서 보여지는 부분
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2", "name", "gender", "age", "bio"],
            },
        ),
    ]
    # 검색 필드
    search_fields = ["email"]
    ordering = []
    filter_horizontal = []

admin.site.register(Users, UserAdmin)
# Group 모델을 등록 해제(사용x)
admin.site.unregister(Group)