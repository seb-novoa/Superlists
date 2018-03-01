from .base import FunctionalTest

class LayoutAndStyling(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        # She notices the input box in nicely center
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            506,
            delta=5
        )

        #She starts a new list ans sees rhw input is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            506,
            delta=5
        )
