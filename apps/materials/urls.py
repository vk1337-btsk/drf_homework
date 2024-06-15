from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.materials.apps import MaterialsConfig
from apps.materials.views.course import CourseViewSet
from apps.materials.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView
from apps.materials.views.subscription import SubscribeAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('subscription/', SubscribeAPIView.as_view(), name='subscription')
]
urlpatterns += router.urls
