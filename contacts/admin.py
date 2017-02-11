from django.contrib import admin

from .models import Contact, Company, Note, Touch, Opportunity
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'email_address', 'phone', 'last_contact_date' )
        }),
        ('Notes', {
            'classes': ('collapse',),
            'fields': ('notes', ),
        }),
        ('Touches', {
            'classes': ('collapse',),
            'fields': ('touches',),
        }),

    )




@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Touch)
class TouchAdmin(admin.ModelAdmin):
    pass

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    pass
