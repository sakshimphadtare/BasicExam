from django.contrib import admin 
from .models import Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email') 
    search_fields = ('name', 'subject', 'email')  
    list_filter = ('subject',)  