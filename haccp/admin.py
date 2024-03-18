from django.contrib import admin
from .models import ToDoItem, objekt_ort, pruef, mangel_art



class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(ToDoItem)
admin.site.register(objekt_ort)
admin.site.register(pruef)
admin.site.register(mangel_art)
