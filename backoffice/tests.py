from django.test import TestCase
from django.test.client import Client

from backoffice.models import Discipline
from bibliography.models import BookCategory


class ViewTests(TestCase):

    def assertResponseOK(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def setUp(self):
        self.client = Client()
        Discipline(name_en='g').save()

    def test_about_page(self):
        self.assertResponseOK('/discipline/1/about/')

    def test_homepage(self):
        self.assertResponseOK('/')

    def test_discipline_homepage(self):
        self.assertResponseOK('/discipline/1/')

    def test_book_list(self):
        self.assertResponseOK('/discipline/1/book/')

    def test_book_list_with_category(self):
        BookCategory(pk=1).save()
        response = self.assertResponseOK('/discipline/1/book/1/')
        self.assertIn('category', response.context)

    def test_category_list(self):
        self.assertResponseOK('/discipline/1/category/')

    def test_subject_list(self):
        self.assertResponseOK('/discipline/1/subject/')

    def test_designer_list(self):
        self.assertResponseOK('/discipline/1/designer/')

    def test_article_list(self):
        self.assertResponseOK('/discipline/1/article/')

    def test_link_list(self):
        self.assertResponseOK('/discipline/1/link/')

    def test_video_list(self):
        self.assertResponseOK('/discipline/1/video/')

    def test_event_list(self):
        self.assertResponseOK('/discipline/1/event/')

    def test_search_page_loads(self):
        self.assertResponseOK('/discipline/1/search/')

    def test_search_ajax_request_returns_partial(self):
        response = self.client.get('/discipline/1/search/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)
        self.assertNotIn("<body", response.content)

    def test_logged_in_user_shouldnt_be_a_guest(self):
        self.client.login(username='user', password='password')
