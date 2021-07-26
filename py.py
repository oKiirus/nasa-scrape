from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)
time.sleep(10)

# list = [12,43,56]
# (0,12) (1,43) (2,56)

def scrape():
    headers = ['name', 'light-years from earth', 'mass', 'stellar magnitude', 'date of discovery']
    planetData = []
    for i in range(0, 444):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for e in soup.find_all('ul', attrs = {'class', 'exoplanet'}):
            li = e.find_all('li')
            temp = []
            for a, b in enumerate(li):
                if a == 0:
                    temp.append(b.find_all('a')[0].contents[0])
                else:
                    try:
                        temp.append(b.contents[0])
                    except:
                        temp.append('')
            planetData.append(temp)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open('anyname.csv', 'w') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planetData)

scrape()
      