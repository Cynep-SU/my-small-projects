from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

def read(url):
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + r'C:\Users\Супер Вася\Desktop\Python\2.0.7_0')
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
    driver.get('https://henchan.pro/')
    elem = driver.find_element_by_name('login_name')
    elem.send_keys('Super login')
    elem = driver.find_element_by_name('login_password')
    elem.send_keys('e44fffdc3ec')
    elem.send_keys(Keys.ENTER)
    driver.get(url)
    elem = driver.find_element_by_id('manga_images')
    elem.click()
    elem = driver.find_element_by_class_name('thumb')
    elem.click()
    elem = driver.find_element_by_id('image')
    html = ''
    while html == '':
        html = str(elem.get_attribute('innerHTML'))
        a = html[html.find('https'): html.find('"></a><img src=')]
        #print(html)
    return a
    # time.sleep(60)

def next_page(url):
    num_page = int(url[-6])
    if url[-7].isalnum() and url[-7] != '0':
        num_page += 10 * int(url[-7])
        a = list(url)
        del a[-7]
    elif str(num_page)[-1] == '9' and num_page < 10 and not url[-7].isalnum():
        a = list(url)
    elif str(num_page)[-1] == '9' and num_page < 10:
        a = list(url)
        del a[-7]
    else:
        a = list(url)
    a[-6] = str(num_page + 1)
    return ''.join(a), num_page


def back_page(url):
    b = True
    num_page = int(url[-6])
    if url[-7].isalnum() and url[-7] != '0':
        num_page += 10 * int(url[-7])
        if num_page != 10:
            a = list(url)
            del a[-7]
            b = False
    if num_page == 10 and b:
        a = list(url)
        a[-7] = '0'
    elif b:
        a = list(url)
    a[-6] = str(num_page - 1)
    return ''.join(a), num_page

a = read('https://henchan.pro/manga/32853-moey-zhene-elfiyke-209-let.html')
print(a)
def max_page(start_page):
    start_page = next_page(start_page)
    for i in range(30):
        start_page = next_page(start_page[0])
        response = requests.get(start_page[0])
        if response.status_code != 200:
            #print('Комикс закончился')
            break
        #print(start_page)
    return start_page[1]
print(max_page(a))