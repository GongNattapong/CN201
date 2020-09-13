from django.contrib import admin
from .models import Subject, Register

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("sid","name","semester","year","count","seat","status")

class RegisterAdmin(admin.ModelAdmin):
    list_display = ("name","course")

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Register, RegisterAdmin)