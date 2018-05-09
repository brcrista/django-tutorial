import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_reject_future_pub_date(self):
        future = timezone.now() + datetime.timedelta(days=30)
        q = Question(pub_date=future)
        self.assertFalse(q.is_new())