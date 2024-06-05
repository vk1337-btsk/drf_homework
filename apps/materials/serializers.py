from rest_framework import serializers

from apps.materials.models import Courses, Lessons


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Courses
        fields = '__all__'

    @staticmethod
    def get_count_lesson(course):
        return Lessons.objects.filter(course=course).count()
