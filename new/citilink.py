import requests
from bs4 import BeautifulSoup
#print('is working')
import json
url = 'https://www.citilink.ru'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
page = soup.prettify()
def pageData():
    num_p_d = page.find('pageData = {"pageType"') + 11
    return json.loads(page[num_p_d:page[num_p_d: num_p_d + 400].rfind('}') + num_p_d + 1])
