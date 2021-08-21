import requests
import xlsxwriter
from bs4 import BeautifulSoup

site = requests.get("http://portal.guap.ru/portal/priem/priem2020/lists/11_193_KO.html")
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'html.parser')
workbook = xlsxwriter.Workbook('res2.xlsx')
worksheet = workbook.add_worksheet()
ones_row_list = soup.findAll('tr')
x = 0
for el in ones_row_list:
    try:
        # print(el)
        # if False:
        if 'align="center"' in str(el):
            x += 1
            soup = BeautifulSoup(str(el), 'html.parser')
            list_ = soup.findAll('td')
            print(list_)
            worksheet.write(f'A{x}', list_[0].contents[0])
            worksheet.write(f'B{x}', list_[1].contents[0])
            worksheet.write(f'C{x}', list_[2].contents[0])
            worksheet.write(f'D{x}', list_[3].contents[0])
            try:
                worksheet.write(f'E{x}', float(list_[4].contents[0]))
            except IndexError:
                worksheet.write(f'E{x}', 0)
    except KeyError:
        pass
workbook.close()
