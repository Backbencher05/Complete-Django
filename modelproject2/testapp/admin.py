from django.contrib import admin
from testapp.models import Employee_Regist

# Register your models here.

class empadmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee_Regist, empadmin)
