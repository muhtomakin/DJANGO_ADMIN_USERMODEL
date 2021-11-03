from django.contrib import admin
from .models import Post
from . import models
from django.contrib import messages

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Database'

class TestAdminPermissions(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):

        if obj != None and request.POST.get('action') == 'delete_selected':
            messages.add_message(request, messages.ERROR, (
                "Are you sure about this?!!!"
            ))

        return True

blog_site = BlogAdminArea(name='BlogAdmin')

admin.site.register(Post)
blog_site.register(models.Post, TestAdminPermissions)
blog_site.register(models.Books)
