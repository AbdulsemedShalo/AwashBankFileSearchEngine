from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(discussionBoard)
admin.site.register(Category)
admin.site.register(Announcements)
admin.site.register(systemAdministrators)
admin.site.register(FileAndDocumentBase)