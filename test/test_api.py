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
    page = requests.get('https://github.com/orgs/django/repositories')
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    first_repo = tree.xpath('(//*[@itemprop="owns"]/following::h3/a)[20]/text()')
    print(first_repo)
    buyers = tree.xpath('//*[@itemprop="owns"]/following::h3/a/text()')
    # #This will create a list of prices
    prices = tree.xpath('//*[@itemprop="owns"]/following::p/text()')
    # title = tree.xpath("//head/title/text()")
    api_resp_dict = {}
    # print('Buyers: ', buyers)
    # print('Prices: ', prices)
    for iter_index in range (0,len(buyers)):
        # epo_name_list_form = older_line.split()
        # repo_name = " ".join(repo_name_list_form)
        new_item_formatted = buyers[iter_index].split()
        repo_name = " ".join(new_item_formatted)

        new_value_formatted = prices[iter_index].split()
        repo_description = " ".join(new_value_formatted)
        api_resp_dict[repo_name] = repo_description
    print(first_repo)
    # print(api_resp_dict)
    # print(api_resp_dict['channels_redis'])
