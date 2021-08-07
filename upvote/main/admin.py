from django.contrib import admin
from .models import Upvote 


# Register your models here.

@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    list_display_links = ['title','id']

    prepopulated_fields = {'slug':('title',)}