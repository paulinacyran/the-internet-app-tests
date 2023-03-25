from helpers.operational_helpers import make_screenshot


def screenshot_decorator(test_function):
    """ Function that wraps a test function and takes a screenshot of the webpage when an AssertionError occurs.

    :param test_function: a function that represents a test case;
    :return: a wrapped version of the test_function that takes a screenshot when an AssertionError occurs;
    """
    def wrapper(self):
        try:
            return test_function(self)
        except AssertionError as ex:
            # Take a screenshot using the make_screenshot function from operational_helpers file
            make_screenshot(self.driver, 'assert')
            raise ex
    return wrapper
