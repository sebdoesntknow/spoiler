from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_retrieve_main_page(self):
        # Get the spoilers homepage
        self.browser.get('http://localhost:8000/spoiler/')
        # Page title and header mention a spoiler
        self.assertIn('Spoiler', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('Spoiler', header_text)
        
        # Invite user to add a new title and spoiler to the database.
#        title_inputbox = self.browser.find_element_by_id('id_new_title')
#        spoiler_inputbox = self.browser.find_element_by_id('id_new_spoiler')
#        self.assertEqual(
#            title_inputbox.get_attribute('title_placeholder'),
#            'Enter a new title'
#        )
#        self.assertEqual(
#            spoiler_inputbox.get_attribute('spoiler_placeholder'),
#            'Enter the title spoiler'
#        )

        # The user adds another spoiler for Game of Thrones
        # in the text box displayed
#        title_inputbox.send_keys('Game of Thrones')
#        spoiler_inputbox.send_keys('The King Joeffrey dies by poison')

        # When the user hits enter the page is refreshed
        # and the spoiler that was just added is displayed
#        title_inputbox.send_keys(Keys.ENTER)

        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
#        self.assertTrue(
#            any(row.text == 'Game of Thrones' for row in rows)
#        )

        # There is still a text box that invites the user to add a new spoiler

        # The page updates again and shows the latest added spoiler.

        # Quit browser after successful tests
        self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
