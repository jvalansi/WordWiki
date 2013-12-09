from django.contrib import admin
from pages.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_filter = ['word']
    search_fields = ['word','word_text']
    
admin.site.register(Page, PageAdmin)