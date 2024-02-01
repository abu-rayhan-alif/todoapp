from django.contrib import admin

# Register your models here.
from .models import Notes

admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):

    list_display=[
     'title','dateTime','description','updatetime',
]