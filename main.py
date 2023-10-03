# from selenium import webdriver
# from bs4 import BeautifulSoup
import pandas as pd
#
# driver = webdriver.Chrome("chromedriver")
#
# path = "https://danso.org/viet-nam/"
x = "year"
y = "population"

data = [
    {
    x : 1985,
    y : 60896721
}, {
    x: 1986,
    y: 62293856
}, {
    x: 1987,
    y: 63701972
}, {
    x: 1988,
    y: 65120439
}, {
    x: 1989,
    y: 66550234
}, {
    x: 1990,
    y: 67988862
}, {
    x: 1991,
    y: 69436954
}, {
    x: 1992,
    y: 70883481
}, {
    x: 1993,
    y: 72300308
}, {
    x: 1994,
    y: 73651218
}, {
    x: 1995,
    y: 74910461
}, {
    x: 1996,
    y: 76068743
}, {
    x: 1997,
    y: 77133214
}, {
    x: 1998,
    y: 78115710
}, {
    x: 1999,
    y: 79035871
}, {
    x: 2000,
    y: 79910412
}, {
    x: 2001,
    y: 80742499
}, {
    x: 2002,
    y: 81534407
}, {
    x: 2003,
    y: 82301656
}, {
    x: 2004,
    y: 83062821
}, {
    x: 2005,
    y: 83832661
}, {
    x: 2006,
    y: 84617540
}, {
    x: 2007,
    y: 85419591
}, {
    x: 2008,
    y: 86243413
}, {
    x: 2009,
    y: 87092252
}, {
    x: 2010,
    y: 87967651
}, {
    x: 2011,
    y: 88871380
}, {
    x: 2012,
    y: 89801926
}, {
    x: 2013,
    y: 90752592
}, {
    x: 2014,
    y: 91713848
}, {
    x: 2015,
    y: 92677076
}, {
    x: 2016,
    y: 93640422
}, {
    x: 2017,
    y: 94600648
}, {
    x: 2018,
    y: 95545962
}, {
    x: 2019,
    y: 96462106
}, {
    x: 2020,
    y: 97338579
}]

year = []
population = []
for i in data:
    year.append(i["year"])
    population.append(i["population"])

print(year)
print(population)

# print(len(year))

# print(len(population))