from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.materials.models import Course, Lesson, Subscription
from apps.users.models.users import Users


class LessonTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Users.objects.create(email="test@test.com", password="12345Qwerty")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Тестовый курс", description="Тестовый курс", owner=self.user)
        self.lesson = Lesson.objects.create(title="Тестовый урок 1", description="Тестовый урок",
                                            url="https://youtube.com/watch_video_lesson", course=self.course,
                                            owner=self.user)

    def test_lesson_create(self):
        # Валидные данные
        data_valid = {
            "title": "Тестовый урок 2",
            "description": "Тестовый урок",
            "url": "https://youtube.com/watch_video_lesson",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_valid)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "id": 2,
            "title": "Тестовый урок 2",
            "description": "Тестовый урок",
            "preview": "http://testserver/media/materials/lessons/preview_lesson_default.jpg",
            "url": "https://youtube.com/watch_video_lesson",
            "course": self.course.pk,
            "owner": self.user.pk
        })

        # Невалидные данные
        data_invalid = {
            "title": "Тестовый урок 3",
            "description": "Тестовый урок",
            "url": "https://site.com",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_invalid)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ["This video is not from YouTube."]})

    def test_lesson_update(self):
        data = {"title": "Тестовый урок 1",
                "description": "Тестовый урок (дописал)",
                "url": "https://youtube.com/watch_video_lesson",
                "course": self.course.pk}

        response = self.client.patch(reverse('materials:lesson_update', kwargs={'pk': self.lesson.pk}),
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Тестовый урок 1",
            "description": "Тестовый урок (дописал)",
            "preview": "http://testserver/media/materials/lessons/preview_lesson_default.jpg",
            "url": "https://youtube.com/watch_video_lesson",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_list(self):
        response = self.client.get(reverse('materials:lesson_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": self.lesson.pk,
                 "title": "Тестовый урок 1",
                 "description": "Тестовый урок",
                 "preview": "http://testserver/media/materials/lessons/preview_lesson_default.jpg",
                 "url": "https://youtube.com/watch_video_lesson",
                 "course": self.course.pk,
                 "owner": self.user.pk
                 }
            ]

        })

    def test_lesson_retrieve(self):
        response = self.client.get(reverse('materials:lesson_detail', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Тестовый урок 1",
            "description": "Тестовый урок",
            "preview": "http://testserver/media/materials/lessons/preview_lesson_default.jpg",
            "url": "https://youtube.com/watch_video_lesson",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_destroy(self):
        response = self.client.delete(reverse('materials:lesson_delete', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.all().exists())


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Users.objects.create(email="test@test.com", password="12345Qwerty")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Курс", description="Тестовый курс", owner=self.user)
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_subscription(self):
        data = {"user": self.user.pk,
                "course": self.course.pk}

        response = self.client.post(reverse('materials:subscription'), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": 'Subscription deactivated'})

        response = self.client.post(reverse('materials:subscription'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": 'Subscription activated'})
