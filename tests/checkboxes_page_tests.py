import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class CheckboxesPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
        self.base_url = "https://the-internet.herokuapp.com/"

    def testFirstCheckbox_whenCheckboxIsSelected_shouldReturnError(self):
        page_url = self.base_url + "checkboxes"
        self.driver.get(page_url)
    
        first_checkbox = self.driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')[0]
        first_checkbox_state = first_checkbox.get_property('checked')
    
        self.assertEqual(False, first_checkbox_state,
                         f"Expected state of the first checkbox: False, differ from actual: {first_checkbox_state},"
                         f" for page url: {self.driver.current_url}.")

    def testSecondCheckbox_whenCheckboxIsUnselected_shouldReturnError(self):
        page_url = self.base_url + "checkboxes"
        self.driver.get(page_url)
    
        second_checkbox = self.driver.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')[1]
        second_checkbox_state = second_checkbox.get_property('checked')
    
        self.assertEqual(True, second_checkbox_state,
                         f"Expected state of the second checkbox: True, differ from actual: {second_checkbox_state},"
                         f" for page url: {self.driver.current_url}.")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()
