from selenium import webdriver
from config.config import Env_Variables

def test_raw():
    driver = webdriver.Firefox(executable_path=Env_Variables['DRIVER_BIN'])
    driver.get(Env_Variables['BASE_URL'])
    page_title = driver.title
    assert page_title == 'Django · GitHub'

    repositories_element = driver.find_element_by_xpath("//a[@class='UnderlineNav-item ' and @href='/orgs/django/repositories']")

    repositories_element.click()
    repositories_section_list = driver.find_elements_by_class_name('Box-row')
    repositories_data_ui = {}
    for section in repositories_section_list:
        repo_name = section.find_element_by_xpath("following::h3/a").text
        # print(repo_name)
        repo_description = section.find_element_by_xpath("following::p").text
        # print(repo_description)
        repositories_data_ui[repo_name] = repo_description

    driver.close()

    print(len(repositories_data_ui))
    print(repositories_data_ui)

