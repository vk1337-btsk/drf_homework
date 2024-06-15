import re

from rest_framework.validators import ValidationError


class UrlLessonsValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube\.com')
        field_value = value.get(self.field)
        if not reg.search(field_value):
            raise ValidationError("This video is not from YouTube.")
