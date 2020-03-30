from django.test import TestCase
from traveleverywhere.models import Question, Blog, Answer
from django.urls import reverse


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

def add_question(title):
        question = Question.objects.get_or_create(title=title)[0]
        question.save()
        return question

def add_answer(text,question):
    answer = Answer.objects.get_or_create(text=text, question=question)[0]
    answer.save()
    return answer

class ForumViewTests(TestCase):

    def test_forum_view_with_no_questions(self):
        """ 
        If no questions exist, the appropriate message should be displayed.
        """ 
        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'There are no questions present.') 
        self.assertQuerysetEqual(response.context['questions'], [])
    
    def test_forum_view_with_questions(self):
        """
        Checks whether questions are displayed correctly when present.
        """
        add_question('How to travel to Ibiza?')
        add_question('When is the best time to go hikig to Ben Nevis?')

        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'How to travel to Ibiza?')
        self.assertContains(response, 'When is the best time to go hikig to Ben Nevis?')
        num_questions = len(response.context['questions'])
        self.assertEquals(num_questions, 2)

    def test_forum_view_for_answers_number(self):
        """
        Checks whether the number of answers for each question are correctly displayed.
        """
        question = add_question('How to travel to Ibiza?')
        add_answer('You could go with WizzAir.', question)
        add_answer('Check in Skyscanner.', question)

        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'How to travel to Ibiza?')
        self.assertEquals(response.context['questions'][0][1], 2)

