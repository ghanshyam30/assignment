# import requests
# import lxml.html

# def test_get():
#     BASE_URI = "https://github.com"
#     ENDPOINT = "/django"

#     URL = BASE_URI + ENDPOINT
#     response = requests.get(URL,stream=True)
#     response.raw.decode_content = True
#     tree = lxml.html.parse(response.raw)
#     first_repo = tree("title")
#     print(first_repo)

from lxml import html
import requests
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
