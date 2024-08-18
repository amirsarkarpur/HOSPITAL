from django.contrib import admin
from .models import doctor,Patient,Medication,AddPrescription,Prescription
# Register your models here.
admin.site.register(doctor)
admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(AddPrescription)
admin.site.register(Prescription)
