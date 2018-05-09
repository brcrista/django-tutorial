import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_old_pub_date_is_not_new(self):
        q = Question(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertFalse(q.is_new())

    def test_new_pub_date_is_new(self):
        q = Question(pub_date=timezone.now() - datetime.timedelta(hours=3))
        self.assertTrue(q.is_new())

    def test_future_pub_date_is_not_new(self):
        future = timezone.now() + datetime.timedelta(days=30)
        q = Question(pub_date=future)
        self.assertFalse(q.is_new())