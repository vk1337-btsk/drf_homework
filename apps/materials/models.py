from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='materials/courses/', default='materials/courses/preview_courses_default.jpg',
                                verbose_name='Превью урока')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        db_table = '_cr_courses'
        ordering = ['title']


class Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс', related_name='course')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='materials/lesson/', default='materials/lesson/preview_lesson_default.jpg',
                                verbose_name='Превью урока')
    url_video = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Укроки'
        db_table = '_cr_lessons'
        ordering = ['title']
