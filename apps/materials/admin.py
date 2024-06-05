from django.contrib import admin
from apps.materials.models import Courses, Lessons


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview',)
    search_fields = ('title',)


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'course')
    list_filter = ('course',)
    search_fields = ('title',)
