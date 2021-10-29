from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Env_Variables
from pages.initialize import initialize

class homePage(initialize):
    
    #Locators
    REPOSITORIES_LOCATOR = "//a[contains(@class,'UnderlineNav-item') and contains(@href,'repositories')]"    
    # Old locator for recerence
    # REPOSITORIES_SECTION_LIST_LOCATOR = "//li[@class='Box-row']"
    REPOSITORIES_SECTION_LIST_LOCATOR = "//*[@itemprop='owns']"
    REPOSITORIES_NAME_LOCATOR = "following::h3/a"
    REPOSITORIES_DESCRIPTION_LOCATOR = "following::p"

    
    def __init__(self):
        super().__init__()
        self.wait_for_element = WebDriverWait(self.driver,20)

    def load(self):
        self.driver.get(Env_Variables.BASE_URL)
    
    def click_repositories(self):
        repository_element = self.driver.find_element_by_xpath(self.REPOSITORIES_LOCATOR)
        repository_element.click()
        self.driver.refresh()
    
    def find_repository_records(self):
        self.wait_for_element.until(EC.presence_of_all_elements_located((By.XPATH,self.REPOSITORIES_SECTION_LIST_LOCATOR)))
        repositories_section_list = self.driver.find_elements_by_xpath(self.REPOSITORIES_SECTION_LIST_LOCATOR)
        # dictionary to store repoository name,description pairs
        repositories_data_ui = {}
        for record in repositories_section_list:            
            try: #Get the repository name
                repo_name = record.find_element_by_xpath("following::h3/a").text
                # print(repo_name)
            except Exception as e:
                print("Repo name not found")
            try: #Get the repository description
                repo_description = record.find_element_by_xpath("following::p").text
                # print(repo_description)
            except Exception as e: # Exception handling
                print("Repo description not fond")
            
            if repo_name and repo_description:
                repositories_data_ui[repo_name] = repo_description
            elif  repo_name and not repo_description:
                repositories_data_ui[repo_name] = "NA"
        
        return len(repositories_section_list)
    
    def closeDriver(self):
        self.driver.close()