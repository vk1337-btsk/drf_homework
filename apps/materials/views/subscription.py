from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.materials.models import Subscription, Course


class SubscribeAPIView(views.APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_obj = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_obj)
        if subs_item.exists():
            subs_item.delete()
            message = 'Subscription deactivated'
        else:
            Subscription.objects.create(user=user, course=course_obj)
            message = 'Subscription activated'
        return Response({"message": message})
