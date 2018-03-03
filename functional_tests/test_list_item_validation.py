from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys

import time

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page ans accidentally tries to submit an empty list item. She hits ENTER on the empty input box
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The home page refreshes, and there is an error message saying that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can´t have an empty list item")

        # She tries again with some test for the item, wich now works
        inputbox = self.get_item_input_box()

        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now dicides to submit a second blank list item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can´t have an empty list item")

        # And she can correct it by filling some text in
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        #Edith goes to the home page and stars a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies', Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies', Keys.ENTER)

        # She sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You´ve already got this in your list")
