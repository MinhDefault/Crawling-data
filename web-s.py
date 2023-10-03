from selenium import webdriver
# from beautifulsoup4 import BeautifulSoup
# from beautifulsoup4 import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('/path/to/chromedriver')

products = []   #List to store name of the product
prices = []     #List to store price of the product
ratings = []    #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):    
    name = a.find('div', attrs={'class':'_4rR01T'})
    price = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    # ratings.append(rating.text) 