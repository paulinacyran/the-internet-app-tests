import unittest
from selenium.webdriver.common.by import By

from helpers.base_test import BaseTest


class TyposPageTests(BaseTest):
    def testParagraph_whenFindsTypo_shouldReturnError(self):
        page_url = self.base_url + "typos"
        self.driver.get(page_url)
    
        paragraph = self.driver.find_elements(By.XPATH, '//*[@class="example"]/p')[1]
        paragraph_text = paragraph.text
    
        expected_paragraph_text = "Sometimes you'll see a typo, other times you won't."
    
        self.assertEqual(expected_paragraph_text, paragraph_text,
                         f"Expected paragraph text differ from actual paragraph text for page url:"
                         f" {self.driver.current_url}. There is a typo in the paragraph text.")


if __name__ == '__main__':
    unittest.main()
    