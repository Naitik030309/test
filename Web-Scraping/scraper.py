from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

STARS_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('C:/Users/Praveen/Downloads/chromedriver')
browser.get(STARS_URL)
time.sleep(10)

def scrape():
    headers = ['v mag.(mv)','proper_name','bayer_designation','distance(ly)','spectral_class','mass(m)','radius(r)','luminosity(l)']
    stars_data = []

    for i in range(0,428):   

        soup = BeautifulSoup(browser.page_source,'html.parser')

        for th_tag in soup.find_all('th',attrs= {'class','headerSort'}):
            tr_tag = th_tag.find_all('tr')

            temp_list = [] 

            for index,tr_tag in enumerate(tr_tag):
                if index == 0:
                    temp_list.append(tr_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append(' ')
        
            stars_data.append(temp_list)
    
    with open('scraper_2.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)

scrape()