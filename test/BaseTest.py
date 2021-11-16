import pytest
import logging
'''
Why do we have base test to use setup fixure?
Reason - so that all test classes can inherit this class and so that for all the classes the setup and teardown will be same
'''
@pytest.mark.usefixtures("setup")
class BaseTest:
    # placeholder method to show that we can put additional functionality required for the tests here
    def myOwnFunction(self):
        logging.info("This is a function from BaseTest class")