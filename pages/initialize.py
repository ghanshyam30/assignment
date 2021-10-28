from selenium import webdriver
from config.config import Env_Variables

class initialize:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=Env_Variables.DRIVER_BIN)
    
    def open_url(self):
        self.driver.get(Env_Variables.BASE_URL)

    def get_driver(self):
        return this.driver
    