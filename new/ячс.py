import requests
from bs4 import BeautifulSoup
user_id = 12345
import json
#what = input()
 
url = 'https://www.citilink.ru'#/search/?text=' + what # url для второй страницы
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(url, headers = headers)
#with open('test.html', 'wb') as output_file:
      #output_file.write(r.text.encode('utf-8'))
soup = BeautifulSoup(r.text, 'html.parser')
page = soup.prettify()
num_p_d = page.find('pageData = {"pageType"') + 11
#if page[page[num_p_d].find('}') + num_p_d] == ' ':
#print(page[page[num_p_d :].find('}') + num_p_d])
print(page[num_p_d:page[num_p_d: num_p_d + 400].rfind('}') + num_p_d + 1])
#print(page[page.find('pageData') + 11: page[page[page.find('pageData') + 11: ].find('}')]])
