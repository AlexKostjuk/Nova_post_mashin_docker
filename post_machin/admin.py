from django.contrib import admin

# Register your models here.
from post_machin.models import PostMachin, Locker

admin.site.register(PostMachin)
admin.site.register(Locker)