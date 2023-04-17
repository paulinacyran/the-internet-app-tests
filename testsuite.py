import unittest

from tests.basic_auth_page_tests import BasicAuthPageTests
from tests.checkboxes_page_tests import CheckboxesPageTests
from tests.disappearing_elements_page_tests import DisappearingElementsPageTests
from tests.drag_and_drop_page_tests import DragAndDropTests
from tests.dynamic_loading_page_tests import DynamicLoadingPageTests
from tests.hovers_page_tests import HoversPageTests
from tests.key_presses_page_tests import KeyPressesPageTests
from tests.login_page_tests import LoginPageTests
from tests.typos_page_tests import TyposPageTests


def all_tests_suite():
    # Initializing the test suite
    test_suite = unittest.TestSuite()
    # Adding tests to the test suite
    test_suite.addTest(unittest.makeSuite(BasicAuthPageTests))
    test_suite.addTest(unittest.makeSuite(CheckboxesPageTests))
    test_suite.addTest(unittest.makeSuite(DisappearingElementsPageTests))
    test_suite.addTest(unittest.makeSuite(DragAndDropTests))
    test_suite.addTest(unittest.makeSuite(DynamicLoadingPageTests))
    test_suite.addTest(unittest.makeSuite(HoversPageTests))
    test_suite.addTest(unittest.makeSuite(KeyPressesPageTests))
    test_suite.addTest(unittest.makeSuite(LoginPageTests))
    test_suite.addTest(unittest.makeSuite(TyposPageTests))
    # Returning the test suite
    return test_suite


if __name__ == '__main__':
    # Initializing a TextTestRunner object
    runner = unittest.TextTestRunner(verbosity=2)
    # Running the test suite
    runner.run(all_tests_suite())
    