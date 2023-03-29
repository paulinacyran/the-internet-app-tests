import unittest
from selenium.webdriver.common.by import By

from helpers.base_test import BaseTest
from helpers.decorators import screenshot_decorator


class BasicAuthPageTests(BaseTest):
    @screenshot_decorator
    def testBasicAuth_whenCredentialsAreValid_shouldAuthorizationBeSuccessful(self):
        username = "admin"
        password = "admin"
        page_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        
        self.driver.get(page_url)

        paragraph = self.driver.find_element(By.XPATH, '//*[@class="example"]/p')
        paragraph_text = paragraph.text

        expected_paragraph_text = "Congratulations! You must have the proper credentials."

        self.assertEqual(expected_paragraph_text, paragraph_text,
                         f"Expected paragraph text differ from actual paragraph text for page url:"
                         f" {self.driver.current_url}.")
       
       
if __name__ == '__main__':
    unittest.main()
    
