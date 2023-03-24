from selenium.webdriver.common.by import By

from helpers import operational_helpers as oh


# Login Page Tests helpers
def user_login(driver, page_url, username, password):
    """ Function to login into a webpage using the specified username and password.

    :param driver: the WebDriver instance;
    :param page_url: the URL of the login page;
    :param username: the username to use for logging in;
    :param password: the password to use for logging in;
    :return: the text of the message that appears after logging in;
    """
    # Navigating to the specified page URL
    driver.get(page_url)
    
    # Finding the username and the password input elements using XPath and storing them in variables
    username_input_element = driver.find_element(By.XPATH, '//input[@id="username"]')
    password_input_element = driver.find_element(By.XPATH, '//input[@id="password"]')
    
    # Finding the login button using XPath and storing it in a variable
    login_button = driver.find_element(By.XPATH, '//button[@class="radius"]')
    
    # Entering the username and password in their respective input fields
    username_input_element.send_keys(username)
    password_input_element.send_keys(password)
    
    # Clicking the login button to submit the form
    login_button.click()
    
    # Waiting for the message element to appear on the page using the wait_for_element from operational helpers
    message_element = oh.wait_for_element(driver, '//div[@id="flash"]')
    
    # Retrieving the text of the message element and storing it in a variable
    message_element_text = message_element.text[0:-2]
    
    # Returning the text of the message element
    return message_element_text
