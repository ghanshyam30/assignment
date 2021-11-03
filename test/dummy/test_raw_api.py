import pytest
from lxml import html
import requests
import json
@pytest.mark.skip
def test_get():
    BASE_URI = "https://github.com"
    ENDPOINT = "/orgs/django/repositories"

    URL = BASE_URI + ENDPOINT
    print(URL)
    page = requests.get(URL)
    # page = requests.get("https://github.com/orgs/django/repositories")
    tree = html.fromstring(page.content)

    #This will create a list of keys which is repository names:    
    repo_name_list = tree.xpath('//*[@itemprop="owns"]/following::h3/a/text()')
    # #This will create a list of repo_description_list
    repo_description_list = tree.xpath('//*[@itemprop="owns"]/following::p/text()')
    # print('repo_name_list: ', repo_name_list)
    # print('repo_description_list: ', repo_description_list)

    #Dummy xpath test
    # title = tree.xpath("//head/title/text()")

    #To store repository name and its description in a dict record
    api_resp_dict = {}
    
    for iter_index in range (0,len(repo_name_list)):
        # format the tab, nextline multispaced string to a concrete one
        new_item_formatted = repo_name_list[iter_index].split()
        repo_name = " ".join(new_item_formatted)

        # format the tab, nextline multispaced string to a concrete one
        new_value_formatted = repo_description_list[iter_index].split()
        repo_description = " ".join(new_value_formatted)

        # Store repository name and descrition against it for better maintenance
        api_resp_dict[repo_name] = repo_description

    print(api_resp_dict['channels_redis'])


@pytest.mark.dict
def test_get_repos():
    BASE_URI = "https://api.github.com"
    ENDPOINT = "/orgs/django/repos"
    header_params ={'accept':'application/vnd.github.v3+json'}

    URL = BASE_URI + ENDPOINT
    # print(URL)
    repo_response_object = requests.get(URL,headers = header_params)
    # print(repo_resp_bytes.text)

    dictionary_response_repos = repo_response_object.json()
    # print(dictionary_response_repos)
    repo_dict = {}
    for item in dictionary_response_repos:
        # print(item['name'])
        repo_name = repo_description =''
        repo_name = item['name']
        repo_description = item['description']        
        repo_dict[repo_name] = repo_description
    print(repo_dict)
