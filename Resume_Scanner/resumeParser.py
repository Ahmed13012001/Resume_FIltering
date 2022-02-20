import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import nltk
from pyresparser import ResumeParser

from bs4 import BeautifulSoup
import requests

def skillExtract(url):
    result = []
    df = pd.read_csv('./ResumeSkill.csv')

    frontEnd = list(df['Front_End'])
    back_End = list(df['Back_End'])
    Android = list(df['Android_Developer'])
    Machine_Learning = list(df['Machine_Learning'])

    data = ResumeParser(url).get_extracted_data()
    skills=data['skills']
    #print(data)
    mail = data['email']
    contact_no = data['mobile_number']
    f_end=0
    b_end=0
    android=0
    ml=0

    for i in skills:
        if i in frontEnd:
            f_end+=1
    for i in skills:
        if i in back_End:
            b_end+=1 
    for i in skills:
        if i in Machine_Learning:
            ml+=1
    for i in skills:
        if i in Android:
            android+=1

    domain_list = []
    domain_list.append(f_end)
    domain_list.append(b_end)
    domain_list.append(ml)
    domain_list.append(android)

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
    capedom = domain.replace(" ","+")
    wipdom = domain.replace(" ","%20")
    waldom = wipdom
    result.append(capedom)
    result.append(wipdom)
    result.append(waldom)
    return result
#skillExtract('resume/Atruba_res.pdf')

    # job_title = domain
    # job_title.replace(" ","%20")
    # location = "India"
