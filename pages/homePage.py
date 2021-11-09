from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Env_Variables
from pages.basePageLib import BasePage
import logging

class homePage(BasePage):
    
    #Locators
    REPOSITORIES_LOCATOR = "//a[contains(@class,'UnderlineNav-item') and contains(@href,'repositories')]"

    PACKAGES_LOCATOR = "//a[contains(@class,'UnderlineNav-item') and contains(@href,'packages')]"
    PROJECTS_LOCATOR = "//a[contains(@class,'UnderlineNav-item') and contains(@href,'projects')]"
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def select_category(self,category_param):
        if "repositor" in category_param.lower():
            set_category = self.REPOSITORIES_LOCATOR
        elif "package" in category_param.lower():
            set_category = self.PACKAGES_LOCATOR
        elif "project" in category_param.lower():
            set_category = self.PROJECTS_LOCATOR
        
        logging.info(f"Selecting category: {set_category}")
        self.click_element(set_category)

        self.driver.refresh()