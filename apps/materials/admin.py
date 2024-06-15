from django.contrib import admin
from apps.materials.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'owner',)
    search_fields = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'course', 'owner',)
    list_filter = ('course', 'owner',)
    search_fields = ('title',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'status',)
    list_filter = ('user', 'course',)
    search_fields = ('user',)
