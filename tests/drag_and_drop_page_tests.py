import unittest
from selenium.webdriver.common.by import By
import os

from helpers.base_test import BaseTest
from helpers.decorators import screenshot_decorator


class DragAndDropTests(BaseTest):
    @screenshot_decorator
    def testDraggableAndDroppableElements_whenIsPossibleToDragAndDrop_shouldReverseElementsTexts(self):
        page_url = self.base_url + "drag_and_drop"
        self.driver.get(page_url)
        
        draggable_element_id = "column-a"
        droppable_element_id = "column-b"

        try:
            with open(os.path.join('helpers', 'js helpers', 'drag_and_drop_helper.js')) as f:
                js = f.read()
        except FileNotFoundError:
            with open(os.path.join('..', 'helpers', 'js helpers', 'drag_and_drop_helper.js')) as f:
                js = f.read()
        
        self.driver.execute_script(js + "$('#%s').simulateDragDrop({ dropTarget: '#%s'});"
                                   % (draggable_element_id, droppable_element_id))

        element_after_drag_and_drop = self.driver.find_elements(By.XPATH, '//*[@class="column"]/header')[0]
        element_after_drag_and_drop_text = element_after_drag_and_drop.text
        
        expected_element_after_drag_and_drop_text = "B"
        
        self.assertEqual(expected_element_after_drag_and_drop_text, element_after_drag_and_drop_text,
                         f"Expected element text differ from actual element text for page url:"
                         f" {self.driver.current_url}.")


if __name__ == '__main__':
    unittest.main()
