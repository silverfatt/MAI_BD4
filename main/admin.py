from django.contrib import admin
from .models import Form, Firm, MedsList, Med, Prescription


class FormAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Form._meta.get_fields()][1:]


class FirmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Firm._meta.get_fields()][1:]


class MedsListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MedsList._meta.get_fields()][1:]


class MedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Med._meta.get_fields()][1:]


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prescription._meta.get_fields()][1:]


admin.site.register(Form, FormAdmin)
admin.site.register(Firm, FirmAdmin)
admin.site.register(MedsList, MedsListAdmin)
admin.site.register(Med, MedAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
