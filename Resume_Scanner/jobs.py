from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(executable_path = f"C:\Program Files (x86)\Inst_Drivers\chromedriver",chrome_options = options)



from bs4 import BeautifulSoup
from resumeParser import skillExtract

domain = skillExtract("resume/Atruba_res.py")

def walmartJb(waldom):
    url = "https://careers.walmart.com/results?q={}&page=1&sort=rank&expand=department,brand,type,rate&jobCareerArea=all".format(waldom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")
    htmls = driver.page_source
    with open("cmpny/wlmrtjb.html","w+", encoding="utf8") as f:
        f.write(htmls)
    
    with open("cmpny/wlmrtjb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("div",class_="search__results")
    cards = page.find_all("li",class_="search-result")

    for card in cards:
        headline = card.find("div",class_="job-listing__headline")
        title = headline.find("h4",class_="job-listing__title").text
        link = headline.find("a").get("href")
        info = card.find("div",class_="job-listing__info")
        location = info.find("span",class_ = "job-listing__location").text
        print(title)
        print(location)
        print(link)


def capeJb(capedom):
    url = "https://www.capgemini.com/in-en/careers/job-search/?search_term={}".format(capedom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")

    htmls = driver.page_source
    with open("cmpny/capejb.html","w+", encoding="utf8") as f:
        f.write(htmls)

    with open("cmpny/capejb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("section",class_="container-full")
    cards = page.find_all("div",class_="card_default__content")

    for card in cards:
        link = card.find("a").get("href")
        a= card.find("h3",class_="card_default__title").text
        #print(type(a))
        if "|" in a:
            title ,expr ,location  = a.split("|")
            print(link)
            print(title)
            print(expr.strip())
            print(location.strip())
        else:
            print(a)
            print(link)
    
def wipJb(wipdom):
    url = "https://careers.wipro.com/careers-home/jobs?keywords={}&stretch=10&stretchUnit=MILES&sortBy=relevance&page=1".format(wipdom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")

    htmls = driver.page_source
    with open("cmpny/wiprojb.html","w+", encoding="utf8") as f:
        f.write(htmls)

    with open("cmpny/wiprojb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("div",class_="search-results")
    data = page.find_all("mat-expansion-panel")
    for i in data:
        title = i.find("p",class_="job-title").text
        job_id = i.find("p",class_="req-id").text
        location = i.find("span",class_="location").text
        templink = i.find("a",class_="mat-focus-indicator")
        link = templink.get("href")
        #desc = i.find("span",class_ = "mat-expansion-indicator").click()
        #a= i.find("div",class_="inner-html-description")
        print(title)
        print(job_id)
        print(location)
        print(link)


waldom = domain[-1]
capedom = domain[0]
wipdom = domain[1]
print(capedom)
if capedom == "Android+Developer":
    capedom = "Java+Developer"
capeJb(capedom)
wipJb(wipdom)
walmartJb(waldom)
#driver.quit()