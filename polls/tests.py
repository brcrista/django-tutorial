import datetime

from django.test import TestCase
from django.urls import reverse
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

def create_question(question_text: str, time_from_now: datetime.timedelta) -> None:
    """Add a question to the list of `Question` objects."""
    pub_date = timezone.now() + time_from_now
    Question.objects.create(question_text=question_text, pub_date=pub_date)

def question_str(question_text: str) -> str:
    """Simulate the string representation of a question."""
    return f'<Question: {question_text}>'

class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_past_question(self):
        create_question('test', datetime.timedelta(days=-1))
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_questions'], [question_str('test')])

    def test_future_question(self):
        create_question('test', datetime.timedelta(days=1))
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_questions'], [])