import unittest

from tests.checkboxes_page_tests import CheckboxesPageTests
from tests.disappearing_elements_page_tests import DisappearingElementsPageTests
from tests.login_page_tests import LoginPageTests
from tests.typos_page_tests import TyposPageTests


def all_tests_suite():
    # Initializing the test suite
    test_suite = unittest.TestSuite()
    # Adding tests to the test suite
    test_suite.addTest(unittest.makeSuite(TyposPageTests))
    test_suite.addTest(unittest.makeSuite(CheckboxesPageTests))
    test_suite.addTest(unittest.makeSuite(LoginPageTests))
    test_suite.addTest(unittest.makeSuite(DisappearingElementsPageTests))
    # Returning the test suite
    return test_suite


if __name__ == '__main__':
    # Initializing a TextTestRunner object
    runner = unittest.TextTestRunner(verbosity=2)
    # Running the test suite
    runner.run(all_tests_suite())
    