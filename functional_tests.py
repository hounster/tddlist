from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith wants to try a new web app.  She hits its homepage:
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention "to-do" lists:
        self.assertIn('To-Do', self.browser.title)

# She is invited to enter a to-do item immediately.

# She types "Buy peacock feathers" into a text box.

# When she hits ENTER, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list.

# There is still a text box inviting her to add another item.  She
# enters "Use peacock feathers to make a fly for fly fishing".

# The page updates again, now both items are in her list.

# Edith wonders if the site will remember her list.  Then notices
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits the URL - her to-do list is still there.

# Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
