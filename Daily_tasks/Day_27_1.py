# Automation using Selenium
# case 1 
# Kerala results

from selenium import webdriver
from time import sleep

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

browser = webdriver.Chrome(executable_path = 'D:\chromedriver')
browser.get(url)
sleep(2)

school_code = browser.find_element_by_name('treg')
school_code.send_keys(2000)
sleep(2)

get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()

html_page = browser.page_source
from bs4 import BeautifulSoup as BS
soup = BS(html_page)
browser.quit()

# case 2
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

browser = webdriver.Chrome(executable_path = 'D:\chromedriver')
browser.get(wiki)

right_table = browser.find_element_by_class_name('wikitable')

A = []
B = []
C = []
D = []
E = []
F = []

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    
    if len(cells) == 6:
        A.append(cells[1].text.strip())
        B.append(states[0].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
import pandas as pd

df = pd.DataFrame()
df['State_UT'] = B
df['Admin_Cap'] = A
df['Legis_Cap'] = C
df['Judi_Cap'] = D
df['Year'] = E
df['Formar_Cap'] = F

browser.quit()