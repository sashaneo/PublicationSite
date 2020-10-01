from django.contrib import admin
from .models import Contact, Publication, FeedbackForm


# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'link')


@admin.register(Publication)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'id')


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ('author_message_name', 'author_message_email', 'message_text', 'message_date')
