from selenium import webdriver


def test_raw():
    driver = webdriver.Firefox(executable_path="/home/thebadcoder/TestWorkspace/drivers/geckodriver")
    driver.get("https://github.com/django")
    page_title = driver.title
    assert page_title == 'Django · GitHub'

    repositories_element = driver.find_element_by_xpath("//a[@class='UnderlineNav-item ' and @href='/orgs/django/repositories']")

    repositories_element.click()
    repositories_section_list = driver.find_elements_by_class_name('Box-row')
    repositories_data_ui = {}
    for section in repositories_section_list:
        repo_name =  ""
        repo_name = section.find_element_by_tag_name("h3").find_element_by_tag_name("a").text
        print(repo_name)
        repo_description = ""
        repo_description = section.find_element_by_xpath("following::p[@itemprop='description']").text
        print(repo_description)
        repositories_data_ui[repo_name] = repo_description

    print(len(repositories_data_ui))
    print(repositories_data_ui)
