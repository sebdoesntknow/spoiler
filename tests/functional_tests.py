from selenium import webdriver
import unittest

browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_retrieve_main_page(self):
        # Get the spoilers homepage
        self.browser.get('http://localhost:8000/spoiler/')

    def test_spoiler_in_the_page_title(self):
        # Page title and header mention a spoiler
        self.assertIn('Spoiler', self.browser.title)
        self.fail('Finish the test!')

        # Invite user to add a new spoiler to the database.

        # The user adds another spoiler for Game of Thrones
        # in the text box displayed

        # When the user hits enter the page is refreshed
        # and the spoiler that was just added is displayed

        # There is still a text box that invites the user to add a new spoiler

        # The page updates again and shows the latest added spoiler.

        # Quit browser after successful tests

if __name__ == '__main__':
    unittest.main(warnings='ignore')
