from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_element(driver, xpath, timeout=10):
    """ Function to wait for an element to be visible on a webpage.

    :param driver: the WebDriver instance;
    :param xpath: the xpath of the element to wait for;
    :param timeout: the number of seconds to wait for the element to be visible;
    :return: the first element that matches the specified XPath and is visible on the webpage;
    """
    # Defining the locator using the XPath provided
    locator = (By.XPATH, xpath)
    # Creating an object that checks whether the element is visible
    element_located = ec.visibility_of_element_located(locator)
    # Initializing a WebDriverWait object with the specified timeout duration
    wait = WebDriverWait(driver, timeout)
    # Defining an error message to be displayed if the element is not found within the specified timeout duration
    timeout_message = f"Element for xpath: '{xpath}' and url: {driver.current_url} not found in {timeout} seconds"
    # Waiting for the element to be visible, and returning it once it is found
    return wait.until(element_located, timeout_message)
