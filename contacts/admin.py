from django.contrib import admin

from .models import Contact, Business, Note
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
