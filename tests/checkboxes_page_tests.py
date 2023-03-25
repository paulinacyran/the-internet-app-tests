import unittest
from selenium.webdriver.common.by import By

from helpers.base_test import BaseTest
from helpers.decorators import screenshot_decorator

class CheckboxesPageTests(BaseTest):
    @screenshot_decorator
    def testFirstCheckbox_whenCheckboxIsSelected_shouldReturnError(self):
        page_url = self.base_url + "checkboxes"
        self.driver.get(page_url)
    
        first_checkbox = self.driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')[0]
        first_checkbox_state = first_checkbox.get_property('checked')
    
        self.assertEqual(False, first_checkbox_state,
                         f"Expected state of the first checkbox: False, differ from actual: {first_checkbox_state},"
                         f" for page url: {self.driver.current_url}.")

    @screenshot_decorator
    def testSecondCheckbox_whenCheckboxIsUnselected_shouldReturnError(self):
        page_url = self.base_url + "checkboxes"
        self.driver.get(page_url)
    
        second_checkbox = self.driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')[1]
        second_checkbox_state = second_checkbox.get_property('checked')
    
        self.assertEqual(True, second_checkbox_state,
                         f"Expected state of the second checkbox: True, differ from actual: {second_checkbox_state},"
                         f" for page url: {self.driver.current_url}.")
       
        
if __name__ == '__main__':
    unittest.main()
