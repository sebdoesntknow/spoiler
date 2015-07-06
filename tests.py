from django.test import TestCase
from django.core.urlresolvers import resolve
from web_spoiler.views import index

class HomePageTest(TestCase):
    def test_root_url_resolves_to_index(self):
        found = resolve('/spoiler/')
        self.assertEqual(found.func, index)


