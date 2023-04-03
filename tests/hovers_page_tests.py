import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from helpers.base_test import BaseTest
from helpers.decorators import screenshot_decorator


class HoversPageTests(BaseTest):
    @screenshot_decorator
    def testHovers_whenAvatarIsHoveredOver_shouldCaptionAppearUnderTheImage(self):
        page_url = self.base_url + "hovers"
        self.driver.get(page_url)

        actions = ActionChains(self.driver)
        
        avatar = self.driver.find_elements(By.XPATH, '//*[@class="figure"]/img')[0]
        actions.move_to_element(avatar)
        actions.perform()
        
        caption = self.driver.find_elements(By.XPATH, '//*[@class="figcaption"]/h5')[0]
        caption_text = caption.text

        expected_caption_text = "name: user1"
        
        self.assertEqual(expected_caption_text, caption_text,
                         f"Expected paragraph text differ from actual paragraph text for page url:"
                         f" {self.driver.current_url}.")


if __name__ == '__main__':
    unittest.main()
    