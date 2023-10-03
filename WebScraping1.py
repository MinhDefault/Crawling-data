from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver")

path = "https://diemthi.vnexpress.net/index/detail/id/"

start_id = 8100000
end_id = 8603100
for i in range(start_id,end_id):
    path_id = path + str(i)
    driver.get(path_id)
    content = driver.page_source
    soup = BeautifulSoup(content)
    names = soup.findAll(class_="o-detail-thisinh")
    if len(str(names)) > 2 :
            file = open("raw_data1.txt", "a",encoding="utf-8")
            file.write(str(names) + "\n" + "\n")
file.close()