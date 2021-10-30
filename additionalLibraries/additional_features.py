from bs4 import BeautifulSoup

class Additional_Functionalities:
    def compare_ui_api_responses(ui_response_dict, api_response_dict):
        matched_records = {key: ui_response_dict[key] for key in ui_response_dict if key in api_response_dict and api_response_dict[key] == ui_response_dict[key]}
        return (len(matched_records))
    
    def convert_html_dict(html_response):
        response = html_response
        # html_resp = response.read()

        parsed_html = BeautifulSoup(response)
        # print(parsed_html.head.title.text)
        section = parsed_html.findAll('div',itemprop="owns")
        
        """
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(open(r'C:/test.htm'))
        for each_div in soup.findAll('div',{'class':'foo'}):
            print(each_div.findAll('div',{'class':'bar'})).encode("utf-8")
        """

        # print(section)
        repo_dict = {}
        for item in section:
            h3_element= item.find('h3')
            a_element = (h3_element.find('a')).get_text()
            # print(a_element)

            try:
                p_element =item.find('p').get_text()
            except:
                p_element = "NA"

            
            try:
                pa_element = (p_element.find('a')).get_text()
            except Exception as e:
                pa_element= ""

            p_element = p_element + pa_element

            a_element_list = str(a_element).split()
            repo_name = " ".join(a_element_list)
            p_element_list = str(p_element).split()
            repo_description = " ".join(p_element_list)
            # print("{}:{}".format(repo_name,repo_description))
            repo_dict[repo_name] = repo_description
        return repo_dict
