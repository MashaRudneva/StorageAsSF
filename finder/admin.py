from django.contrib import admin

from .models import Storage, Platform, Category, Domain, SiteSettings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm


class SiteSettingsInlineForm(ModelForm):

    #  subtitle_homepage = forms.Textarea(label="subtitle_homepage", max_length=255)

    def __init__(self, *args, **kwargs):
        super(SiteSettingsInlineForm, self).__init__(*args, **kwargs)
        self.fields['subtitle_homepage'].widget.attrs['style'] = 'width:90%;height:100px'


class SiteSettingsAdmin(admin.ModelAdmin):

    form = SiteSettingsInlineForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_add_permission(self, request, obj=None):
        # Disable delete
        return False

# Register your models here.


class MyUserChangeForm(UserChangeForm):
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return None


class MyUserCreationForm(UserCreationForm):

    email = forms.CharField(required=False, label="Email", max_length=255)

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'
        password = make_password('')
        self.fields['password1'].widget.attrs['value'] = password
        self.fields['password2'].widget.attrs['value'] = password
        self.fields['password1'].widget.attrs['readonly'] = True
        self.fields['password2'].widget.attrs['readonly'] = True


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', )
    search_fields = ('username', 'email')

    form = MyUserChangeForm
    add_form = MyUserCreationForm


class MyModelAdmin(admin.ModelAdmin):
    pass

    # def has_view_permission(self, request, obj=None):
    #     perm = show_only_allow_institute_data(request)
    #     if perm:
    #         return super().has_view_permission(request, obj)
    #     return perm

    # def has_change_permission(self, request, obj=None):
    #     perm = show_only_allow_institute_data(request)
    #     if perm:
    #         return super().has_change_permission(request, obj)
    #     return perm

    # def has_delete_permission(self, request, obj=None):
    #     perm = show_only_allow_institute_data(request)
    #     if perm:
    #         return super().has_change_permission(request, obj)
    #     return perm

    # def has_add_permission(self, request):
    #     perm = show_only_allow_institute_data(request)
    #     if perm:
    #         return super().has_add_permission(request)
    #     return perm


class CategoryAdmin(MyModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class PlatformAdmin(MyModelAdmin):

    list_display = ('name',)
    search_fields = ['name']


class DomainAdmin(MyModelAdmin):

    list_display = ('name',)
    search_fields = ['name']




class StorageAdmin(MyModelAdmin):

    def category(self):
        category = ','.join([g.name for g in self.categories.all()]) if self.categories.count() else ''
        return (category[:40] + '..') if len(category) > 40 else category

    list_display = ('name', 'description', category)
    search_fields = ['name']

    filter_horizontal = ('platforms', 'categories', 'domain')



admin.site.register(SiteSettings, SiteSettingsAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Storage, StorageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Domain, DomainAdmin)
