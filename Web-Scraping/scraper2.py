from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')

def scrape():
    headers = ['Name','Distance','Mass','Radius']
    stars_data = []

    for i in range(0,428):   

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