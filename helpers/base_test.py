import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
        self.base_url = "https://the-internet.herokuapp.com/"
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()