import pytest
from selenium import webdriver
from config.config import Env_Variables

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Firefox(executable_path=Env_Variables.DRIVER_BIN)
    driver.get(Env_Variables.BASE_URL)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def some_stuff(self):
        title = self.driver.title
        print(title)

class Test_google(BaseTest):
    def test_gogle_title(self):
        self.driver.get("https://www.google.com")
        title = self.driver.title
        print(title)