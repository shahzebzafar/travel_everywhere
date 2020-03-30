from django.test import TestCase
from traveleverywhere.models import Question, Blog

class QuestionModelTests(TestCase):
    
    def test_question_slug_creation(self):
        """
        Checks to make sure when a question is created,
        an approriate slug is created as well.
        For example, "Slug should have dashes" should look like
        "slug-should-have-dashes".
        """
        question = Question(title="Slug should have dashes")
        question.save()

        self.assertEqual(question.slug, "slug-should-have-dashes")

class BlogModelTests(TestCase):

    def test_blog_slug_creation(self):
        """
        Checks to make sure when a blog is created,
        an approriate slug is created as well.
        For example, "Slug should have dashes" should look like
        "slug-should-have-dashes".
        """
        blog = Blog(title="Slug should have dashes")
        blog.save()

        self.assertEqual(blog.slug, "slug-should-have-dashes")
    