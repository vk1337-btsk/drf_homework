from rest_framework import serializers, fields

from apps.materials.serializers.lesson import LessonSerializer
from apps.materials.validators import UrlLessonsValidator
from apps.materials.models import Course, Lesson, Subscription


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = fields.SerializerMethodField()
    is_subscribed = fields.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [UrlLessonsValidator(field='url')]

    @staticmethod
    def get_count_lesson(course):
        return Lesson.objects.filter(course=course).count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    def create(self, validated_data):
        lessons_data = validated_data.pop('lesson_list', [])
        course = Course.objects.create(**validated_data)
        for lesson_data in lessons_data:
            Lesson.objects.create(course=course, **lesson_data)
        return course
