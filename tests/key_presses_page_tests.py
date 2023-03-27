import unittest
from selenium.webdriver.common.keys import Keys

from helpers.base_test import BaseTest
from helpers import functional_helpers as fh
from helpers.decorators import screenshot_decorator


class KeyPressesPageTests(BaseTest):
    @screenshot_decorator
    def testPressingShiftKey_whenResultTextIsNotAsExpected_shouldReturnError(self):
        page_url = self.base_url + "key_presses?"
        key = Keys.SHIFT

        result_text = fh.find_result_text(self.driver, page_url, key)
        expected_result_text = "You entered: SHIFT"

        self.assert_result_text(expected_result_text, result_text)

    @screenshot_decorator
    def testPressingLeftArrowKey_whenResultTextIsNotAsExpected_shouldReturnError(self):
        page_url = self.base_url + "key_presses?"
        key = Keys.ARROW_LEFT

        result_text = fh.find_result_text(self.driver, page_url, key)
        expected_result_text = "You entered: LEFT"

        self.assert_result_text(expected_result_text, result_text)
    
    @screenshot_decorator
    def testPressingZKey_whenResultTextIsNotAsExpected_shouldReturnError(self):
        page_url = self.base_url + "key_presses?"
        key = "Z"

        result_text = fh.find_result_text(self.driver, page_url, key)
        expected_result_text = "You entered: Z"

        self.assert_result_text(expected_result_text, result_text)
        
    def assert_result_text(self, expected_result_text, result_text):
        self.assertEqual(expected_result_text, result_text,
                         f"Expected result text: '{expected_result_text}' differ from actual:"
                         f" '{result_text}', for page url: {self.driver.current_url}.")


if __name__ == '__main__':
    unittest.main()
