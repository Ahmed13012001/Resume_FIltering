from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import nltk
from pyresparser import ResumeParser

from bs4 import BeautifulSoup
import requests

def skillExtract(url):
    result = []
    df = pd.read_csv('Resume_Filtering\ResumeSkill.csv')

    data = ResumeParser(url).get_extracted_data()
    print(data)
    skills=data['skills']
    low_skills = list(map(lambda x: x.lower(), skills))
    totexp = data['total_experience']
    exper = data['experience']
    mail = data['email']
    degree = data['degree']
    print("degree is ",degree)
    deg = ['Mechanical Engineering']
    deg2 = ["mechanical engineering"]
    if degree != None:
        if deg in degree or deg2 in low_skills :
            if totexp>1:
                domain = exper[1]
            
            else:
                Quality_Engineer = list(df['Quality_Engineer'])
                Production_Engineer = list(df['Production_Engineer'])
                Design_Engineer = list(df['Design_Engineer'])
                Maintenance_Engineer = list(df['Maintenance_Engineer'])
                Hvac_Engineer = list(df['Hvac_Engineer'])
                qual = 0
                prod = 0
                maint = 0
                design = 0
                hvac = 0
    
                for i in skills:
                    if i in Android:
                        android+=1
                    
                for i in skills:
                    if i in Quality_Engineer:
                        qual+=1
                        
                for i in skills:
                    if i in Production_Engineer:
                        prod+=1
                        
                for i in skills:
                    if i in Design_Engineer:
                        design+=1
                    
                for i in skills:
                    if i in Maintenance_Engineer:
                        maint+=1
                    
                for i in skills:
                    if i in Hvac_Engineer:
                        hvac+=1
                    
                domain_list =[]
                domain_list.append(qual)
                domain_list.append(prod)
                domain_list.append(design)
                domain_list.append(maint)
                domain_list.append(hvac)
                domain_val = 0
                domain_max = max(qual,prod,design,maint,hvac)
                for i in range(len(domain_list)):
                    if domain_max == domain_list[i]:
                        domain_val = i
                if domain_val==0:
                    domain = "Quality Engineer"
                elif domain_val==1:
                    domain = "Production Engineer"
                elif domain_val==2:
                    domain = "Design Engineer"
                elif domain_val==3:
                    domain = "Maintenance Engineer"
                elif domain_val==4:
                    domain = "Hvac Engineer"
            capedom = domain.replace(" ","+")
            wipdom = domain.replace(" ","%20")
            waldom = wipdom
            result.append(capedom)
            result.append(wipdom)
            result.append(waldom)
            return result

        elif 'computer science' in low_skills or 'Java' in skills or 'Python' in skills or "C" in skills or 'Html5' in skills or 'Android' in skills:
        
            print("Im Here!!!!!!!!!")
            if totexp>4:
                domain = exper[1]
                
            else:
                frontEnd = list(df['Front_End'])
                back_End = list(df['Back_End'])
                Android = list(df['Android_Developer'])
                Machine_Learning = list(df['Machine_Learning'])
                f_end=0
                b_end=0
                android=0
                ml=0
                # skillsList = []
                for i in skills:
                    if i in frontEnd:
                        f_end+=1                 
                for i in skills:
                    if i in back_End:
                        b_end+=1 
                        # print('bend',i)
                        # skillsList.append(i)
                for i in skills:
                    if i in back_End:
                        android+=1 
                        # print('Androird',i)    
                for i in skills:
                    if i in Machine_Learning:
                        ml+=1
                        # print('ml',i)
                        # skillsList.append(i)
                domain_list = []
                domain_list.append(f_end)
                domain_list.append(b_end)
                domain_list.append(ml)
                domain_list.append(android)
                print(domain_list)
                domain_val = 0
                domain_max = max(f_end,b_end,ml,android)
                for i in range(len(domain_list)):
                    if domain_max == domain_list[i]:
                        domain_val = i
                if domain_val==0:
                    domain = "FrontEnd Developer"
                elif domain_val==1:
                    domain = "BackEnd Developer"
                elif domain_val==2:
                    domain = "Machine Learning"
                elif domain_val==3:
                    domain = "Android Developer"
            print("Domain Is " ,domain)
            capedom = domain.replace(" ","+")
            wipdom = domain.replace(" ","%20")
            waldom = wipdom
            result.append(capedom)
            result.append(wipdom)
            result.append(waldom)
            return result


options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(executable_path = f"C:\Program Files (x86)\Inst_Drivers\chromedriver",chrome_options = options)



from bs4 import BeautifulSoup

#domain = skillExtract("resume/ShumeelMomin_MechEng.pdf")

def walmartJb(waldom):
    url = "https://careers.walmart.com/results?q={}&page=1&sort=rank&expand=department,brand,type,rate&jobCareerArea=all".format(waldom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")
    print("WALMART JOBS")
    htmls = driver.page_source
    with open("cmpny/wlmrtjb.html","w+", encoding="utf8") as f:
        f.write(htmls)
    
    with open("cmpny/wlmrtjb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("div",class_="search__results")
    cards = page.find_all("li",class_="search-result")
    # headline = []
    title = []
    link = []
    location = []
    # initial = "https://careers.walmart.com"
    for card in cards:
        headline = card.find("div",class_="job-listing__headline")
        tit = headline.find("h4",class_="job-listing__title").text
        lnk = headline.find("a").get("href")
        info = card.find("div",class_="job-listing__info")
        loc = info.find("span",class_ = "job-listing__location").text
        title.append(tit)
        location.append(loc)
        # lnk = initial+lnk
        link.append(lnk)
        # print(title)
        # print(location)
        # print(link)
        print("=============================================================")
    return title , location,link

# def capeJb(capedom):
#     url = "https://www.capgemini.com/in-en/careers/job-search/?search_term={}".format(capedom)
#     driver.get(url)
#     driver.execute_script("window.scrollTo(1,20)")
#     print("CAPEGIMINI JOBS")
#     htmls = driver.page_source
#     with open("cmpny/capejb.html","w+", encoding="utf8") as f:
#         f.write(htmls)

#     with open("cmpny/capejb.html",encoding="utf8") as f:
#         page = f.read()
#     soup = BeautifulSoup(page,"html.parser")
#     page = soup.find("section",class_="container-full")
#     cards = page.find_all("div",class_="card_default__content")

#     for card in cards:
#         link = card.find("a").get("href")
#         a= card.find("h3",class_="card_default__title").text
#         #print(type(a))
#         if "|" in a:
#             title ,expr ,location  = a.split("|")
#             print(link)
#             print(title)
#             print(expr.strip())
#             print(location.strip())
#             print("=============================================================")
#         else:
#             print(a)
#             print(link)
#             print("=============================================================")
    
def wipJb(wipdom):
    url = "https://careers.wipro.com/careers-home/jobs?keywords={}&stretch=10&stretchUnit=MILES&sortBy=relevance&page=1".format(wipdom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")
    print("WIPRO JOBS")
    htmls = driver.page_source
    with open("cmpny/wiprojb.html","w+", encoding="utf8") as f:
        f.write(htmls)

    with open("cmpny/wiprojb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("div",class_="search-results")
    data = page.find_all("mat-expansion-panel")
    title = []
    location = []
    link = []
    # initial = "https://careers.wipro.com"
    for i in data:
        tit = i.find("p",class_="job-title").text
        job_id = i.find("p",class_="req-id").text
        loc = i.find("span",class_="location").text
        templink = i.find("a",class_="mat-focus-indicator")
        lnk = templink.get("href")
        #desc = i.find("span",class_ = "mat-expansion-indicator").click()
        #a= i.find("div",class_="inner-html-description")
        title.append(tit)
        # lnk = initial + lnk
        link.append(lnk)
        location.append(loc)
        # print(title)
        # print(job_id)
        # print(location)
        # print(link)
        print("=============================================================")
    return title , location,link


def ltijb(ltidom):
    url = "https://careers.lntinfotech.com/search/?createNewAlert=false&q={}&optionsFacetsDD_country=&optionsFacetsDD_location=&locationsearch=".format(ltidom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")
    print("LTI Jobs")
    htmls = driver.page_source
    with open("cmpny/ltijb.html","w+", encoding="utf8") as f:
        f.write(htmls)

    with open("cmpny/ltijb.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    table = soup.find("table",class_="searchResults")
    rows = table.find_all("tr",class_="clickable")
    title = []
    location = []
    link = []
    initial = "https://careers.lntinfotech.com"
    for row in rows:
        colTitle = row.find("td",class_="colTitle")
        lnk = colTitle.find("a").get("href")
        tit = colTitle.find("a").text
        loc = colTitle.find("span",class_="jobLocation").text.strip()
        title.append(tit)
        location.append(loc)
        lnk = initial+lnk
        link.append(lnk)
        # print(title)
        # print(link)
        # print(location)
        print("=============================================================")
    return title , location,link


def seimensjob(seimendom):
    print("SEIMENS JOBS")
    url = "https://jobs.siemens.com/jobs?keywords={}&sortBy=relevance&page=1".format(seimendom)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,20)")
    htmls = driver.page_source
    with open("cmpny/siemen.html","w+",encoding="utf8") as f:
        f.write(htmls)
    with open("cmpny/siemen.html",encoding="utf8") as f:
        page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    page = soup.find("div",class_="search-results")
    rows = page.find_all("mat-expansion-panel-header",class_="mat-expansion-panel-header")
    title = []
    location = []
    link = []
    initial = "https://jobs.siemens.com"
    for row in rows:
        content = row.find("span",class_="mat-content")
        tit_cont = content.find("p",class_="job-title")
        link_cont = tit_cont.find("a",class_="job-title-link")
        lnk = link_cont.get('href')
        
        print(type(lnk))
        tit = tit_cont.find("span").text
        abv_cnt = content.find("div",class_="description-container")
        loc = abv_cnt.find("p",class_="label-container").text
        category = abv_cnt.find("span",class_="categories").text
        title.append(tit)
        location.append(loc)
        lnk = initial + lnk
        print(lnk)
        link.append(lnk)
        # print(tit)
        # print(lnk)
        # print(loc)
        # print(category)
        print("--------------------------------------------------------------------------------------------------------")
    return title , location,link
    
# domain = skillExtract("media\ShumeelMomin_MechEng.pdf")
# waldom = domain[-1]
# capedom = domain[0]
# wipdom = domain[1]
# ltidom = capedom
# seimendom = wipdom
# print(capedom)
# if capedom == "Android+Developer":
#     capedom = "Java+Developer"
# ltijb(ltidom)
# capeJb(capedom)
# wipJb(wipdom)
# walmartJb(waldom)
# seimensjob(seimendom)
# wiptitle , wiploc , wiplink = wipJb(wipdom)
# print(wiptitle)
# littitle , ltiloc , ltilink = ltijb(ltidom)
# waltitle , walloc , wallink = walmartJb(waldom)
# seititle , seiloc , seilink = seimensjob(seimendom)
# driver.quit()