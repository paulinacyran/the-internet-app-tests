import unittest
from selenium.webdriver.common.by import By

from helpers.base_test import BaseTest
from helpers.decorators import screenshot_decorator
from helpers import operational_helpers as oh


class DynamicLoadingPageTests(BaseTest):
    @screenshot_decorator
    def testDynamicLoading_whenLoadingBarDisappear_shouldFinishElementTextDisplayed(self):
        page_url = self.base_url + "dynamic_loading/2"
        self.driver.get(page_url)
        
        start_button = self.driver.find_element(By.XPATH, '//*[@id="start"]/button')
        start_button.click()

        finish_element = oh.wait_for_element(self.driver, '//*[@id="finish"]/h4')
        finish_element_text = finish_element.text
        
        expected_finish_element_text = "Hello World!"
        
        self.assertEqual(expected_finish_element_text, finish_element_text,
                         f"Expected finish element text differ from actual finish element text for page url:"
                         f" {self.driver.current_url}.")


if __name__ == '__main__':
    unittest.main()