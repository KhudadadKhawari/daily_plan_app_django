from django.contrib import admin
from .models import Archive, EducationalNote, PersonalNote, BusinessNote

# Register your models here.
admin.site.register(Archive)
admin.site.register(EducationalNote)
admin.site.register(PersonalNote)
admin.site.register(BusinessNote)