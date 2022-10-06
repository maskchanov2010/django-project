from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 15


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'evaluations1', 'evaluations2']
    list_editable = ['evaluations1', 'evaluations2']
    search_fields = ['name']
    list_per_page = 15


class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 15


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['date_beginning','type2',  'date_end', 'tutor']
    list_editable = ['type2', 'date_end', 'tutor']
    list_per_page = 15


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['type2', 'date_end', 'evaluations1', 'evaluations2']
    list_editable = ['date_end', 'evaluations1', 'evaluations2']
    list_per_page = 15


admin.site.register(Category, CategoryAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(History, HistoryAdmin)
