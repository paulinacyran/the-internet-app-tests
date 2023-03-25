import unittest
from selenium.webdriver.common.by import By

from helpers.base_test import BaseTest


class DisappearingElementsPageTests(BaseTest):
    def testNumberOfElements_whenIsNotAsExpected_shouldReturnError(self):
        page_url = self.base_url + "disappearing_elements"
        self.driver.get(page_url)
    
        list_elements = self.driver.find_elements(By.XPATH, '//ul/li')
        list_elements_number = len(list_elements)
    
        expected_list_elements_number = 5
    
        self.assertEqual(expected_list_elements_number, list_elements_number,
                         f" Expected number of the elements on the page: {expected_list_elements_number}"
                         f" differ from actual: {list_elements_number}, for page url: {self.driver.current_url}.")
    

if __name__ == '__main__':
    unittest.main()
    