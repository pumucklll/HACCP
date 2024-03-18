from django.contrib import admin
from .models import Audit_Ereignis, ObjektOrt, Audit, MangelArt, Checkliste, Benutzer



class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Audit_Ereignis)
admin.site.register(ObjektOrt)
admin.site.register(Audit)
admin.site.register(MangelArt)
admin.site.register(Checkliste)
admin.site.register(Benutzer)