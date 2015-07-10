from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.utils import timezone

from .views import index
from .models import Title, Spoiler

# Must create both title and some spoiler because
# template won't show anything if both objects aren't picked up.
def create_title(title="Movie", spoiler="Nasty spoiler", time=timezone.now()):
    new_title = Title(title_text=title, sub_date=time)
    new_title.save()
    return new_title.spoiler_set.create(spoiler_text=spoiler, pub_date=time)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_index(self):
        found = resolve('/spoiler/')
        self.assertEqual(found.func, index)

    def test_homepage_returns_correct_html(self):
        create_title("A Movie", "A movie Spoiler")
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Spoiler</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
