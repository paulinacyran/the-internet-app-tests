import unittest

from helpers.base_test import BaseTest
from helpers import functional_helpers as fh
from helpers.decorators import screenshot_decorator

class LoginPageTests(BaseTest):
    @screenshot_decorator
    def testLoginForm_whenLoginIsValidAndPasswordIsValid_shouldSuccessfulLogin(self):
        page_url = self.base_url + "login"
        username = "tomsmith"
        password = "SuperSecretPassword!"
    
        message_element_text = fh.user_login(self.driver, page_url, username, password)
        expected_message_element_text = "You logged into a secure area!"
    
        self.assert_message_element_text(expected_message_element_text, message_element_text)

    @screenshot_decorator
    def testLoginForm_whenLoginIsValidAndPasswordIsInvalid_shouldShowErrorMessage(self):
        page_url = self.base_url + "login"
        username = "tomsmith"
        password = "SuperPassword!"
    
        message_element_text = fh.user_login(self.driver, page_url, username, password)
        expected_message_element_text = "Your password is invalid!"
    
        self.assert_message_element_text(expected_message_element_text, message_element_text)

    @screenshot_decorator
    def testLoginForm_whenLoginIsInvalidAndPasswordIsValid_shouldShowErrorMessage(self):
        page_url = self.base_url + "login"
        username = "tommysmith"
        password = "SuperSecretPassword!"
    
        message_element_text = fh.user_login(self.driver, page_url, username, password)
        expected_message_element_text = "Your username is invalid!"
    
        self.assert_message_element_text(expected_message_element_text, message_element_text)

    @screenshot_decorator
    def testLoginForm_whenLoginIsInvalidAndPasswordIsInvalid_shouldShowErrorMessage(self):
        page_url = self.base_url + "login"
        username = "tommysmith"
        password = "SuperPassword!"
    
        message_element_text = fh.user_login(self.driver, page_url, username, password)
        expected_message_element_text = "Your username is invalid!"
    
        self.assert_message_element_text(expected_message_element_text, message_element_text)

    def assert_message_element_text(self, expected_message_element_text, message_element_text):
        self.assertEqual(expected_message_element_text, message_element_text,
                         f"Expected message text: '{expected_message_element_text}' differ from actual:"
                         f" '{message_element_text}', for page url: {self.driver.current_url}.")
    

if __name__ == '__main__':
    unittest.main()
    