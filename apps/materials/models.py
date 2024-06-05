from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='materials/courses/', default='materials/courses/preview_course_default.jpg',
                                verbose_name='Превью урока')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        db_table = '_cr_courses'
        ordering = ['title']


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='materials/lessons/', default='materials/lessons/preview_lesson_default.jpg',
                                verbose_name='Превью урока')
    url = models.URLField(**NULLABLE, verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        db_table = '_cr_lessons'
        ordering = ['title']
