import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TyposPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
        self.base_url = "https://the-internet.herokuapp.com/"

    def testParagraph_whenFindsTypo_shouldReturnError(self):
        page_url = self.base_url + "typos"
        self.driver.get(page_url)
    
        paragraph = self.driver.find_elements(By.XPATH, '//*[@class="example"]/p')[1]
        paragraph_text = paragraph.text
    
        expected_paragraph_text = "Sometimes you'll see a typo, other times you won't."
    
        self.assertEqual(expected_paragraph_text, paragraph_text,
                         f"Expected paragraph text differ from actual paragraph text for page url:"
                         f" {self.driver.current_url}. There is a typo in the paragraph text.")
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    