from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import connection
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import signupuser
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser
from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.metrics.pairwise import cosine_similarity
import tempfile
from .models import FileUpload
# from RESUME_FILTERIING.pythonmodules.jobs import walmartJb
# from RESUME_FILTERIING.pythonmodules.jobs import skillExtract
# from .forms import signupuserForm
import os
# from Resume_Filtering.models import signupuser
initialdir = os.getcwd()

from django.contrib.auth import logout

def logout_view(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return redirect(request,'index.html')
    
def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

def resumes(request):
    return render(request,'upload.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def recruitersignup(request):
    return render(request,'recruiterlogin.html')

def recruiterlogin(request):
    return render(request,'HRlogin.html')

def resumeupload(request):
    return render(request,'upload.html')

def logincheck(request):
    if request.method=='POST':
        print(request.POST.get('submit'))
        if request.POST.get('submit') == 'login':
            if request.POST.get('email') and request.POST.get('pass'):
                name = request.POST['email']
                pwd = request.POST['pass']
                with connection.cursor() as cursor:
                    query="Select * from signupuser where umail=%s and pass=%s"
                    cursor.execute(query,[name,pwd])
                    row = cursor.fetchall()
                    print(len(row))
                    if len(row)==1:
                        que = "Select uid from signupuser where umail=%s and pass =%s"
                        cursor.execute(que,[name,pwd])
                        uid = cursor.fetchone()
                        print("User Id Is" , uid )
                        uid = str(uid)
                        userid = ''
                        for i in uid:
                            if i.isdigit():
                                userid += i
                        userid = int(userid)
                        print("integer userid is",userid)
                        # filepath = cursor.fetchone()
                    # que = "INSERT INTO loggedin(name) VALUES (%s)"
                        #cursor.execute(que,[name])
                        #messages.info(request, 'Successfully Logged in !!')
                        print("Done Login !!!")
                        request.session['name'] = name
                        request.session['password'] = pwd
                        # print(filepath)
                        return render(request,'jobsShow.html',{'name':name})
                    else:
                        messages.info(request, 'User Doesnot exist , Please Sign up !!')
                        print("User doesnt Exist ")
                        return render(request,'login.html')
            else:
                return render(request,'login.html')
        elif request.POST.get('submit') == 'Submit':
            uname = request.POST['uname']
            print(uname)
            print('Im here!!!!!!!!!')
            email = request.POST['email']
            pwd = request.POST['pass']
            uploaded_file = request.FILES['document']
            name = uploaded_file.name
            filepath = initialdir+'/media/'+name
            print(filepath)
            print(name)
            
            with connection.cursor() as cursor:
                checkquery = "select * from signupuser where umail=%s and pass=%s"
                cursor.execute(checkquery,[email,pwd])
                row = cursor.fetchall()
                print(len(row))
                if len(row)==1:
                    messages.info(request, 'User Already exist plz Login')
                    print("User Already Exist!!!")
                    return render(request,'login.html')
                else:
                    fs = FileSystemStorage()
                    fs.save(uploaded_file.name, uploaded_file)
                    query = "INSERT INTO `signupuser`( uname, umail , pass,filename ,filepath) VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(query,[uname , email,pwd,name,filepath])
                    print("DOne Registration !!!")
                    request.session['name'] = uname
                    request.session['password'] = pwd
                    messages.info(request, 'Registration done successfully!')
                    return render(request,'jobsShow.html',{'filepath':filepath})

from .jobs import skillExtract

from .jobs import wipJb
from .jobs import ltijb
from .jobs import walmartJb
from .jobs import seimensjob

def wipjobs(request):
    mail = request.session['name']
    print(mail)
    with connection.cursor() as cursor:
        query="Select filepath from signupuser where umail = %s"
        cursor.execute(query,[mail])
        filepath = cursor.fetchall()
    print(type(filepath))
    print(filepath[0])
    fp = str(filepath[0])
    fp = fp.replace('(','')
    
    fp = fp.replace("'",'')
    fp = fp.replace(',','')
    fp = fp.replace(')','')
    print(fp)
    domain = skillExtract(fp)
    print(domain)
    print(type(domain))
    
    wipdom = domain[1]
    wiptitle , wiploc , wiplink = wipJb(wipdom)
    wipro = {
        'wiptitle':wiptitle,
        'wiploc' : wiploc,
        'wiplink' :  wiplink
    }
    lst = [1,2,3,4,5,6,7,8,9,10]
    print(wiptitle)

    return render(request,'wipjobs.html',wipro) 

def waljobs(request):
    mail = request.session['name']
    print(mail)
    with connection.cursor() as cursor:
        query="Select filepath from signupuser where umail = %s"
        cursor.execute(query,[mail])
        filepath = cursor.fetchall()
    # print(type(filepath))
    # print(filepath[0])
    fp = str(filepath[0])
    fp = fp.replace('(','')
    
    fp = fp.replace("'",'')
    fp = fp.replace(',','')
    fp = fp.replace(')','')
    # print(fp)
    domain = skillExtract(fp)
    waldom = domain[-1]
    capedom = domain[0]
    wipdom = domain[1]
    ltidom = capedom
    seimendom = wipdom
    waltitle , walloc , wallink = walmartJb(waldom)
    walmart = {
        'waltitle':waltitle,
        'walloc' : walloc,
        'wallink' :  wallink
    }
    lst = [1,2,3,4,5,6,7,8,9,10]
    # print(waltitle)

    return render(request,'walmartjobs.html',walmart) 


def seijobs(request):
    mail = request.session['name']
    print(mail)
    with connection.cursor() as cursor:
        query="Select filepath from signupuser where umail = %s"
        cursor.execute(query,[mail])
        filepath = cursor.fetchall()
    #print(type(filepath))
    #print(filepath[0])
    fp = str(filepath[0])
    fp = fp.replace('(','')
    
    fp = fp.replace("'",'')
    fp = fp.replace(',','')
    fp = fp.replace(')','')
    # print(fp)
    domain = skillExtract(fp)
    waldom = domain[-1]
    capedom = domain[0]
    wipdom = domain[1]
    ltidom = capedom
    seimendom = wipdom
    

    seititle , seiloc , seilink = seimensjob(waldom)
    seimens = {
        'seititle':seititle,
        'seiloc' : seiloc,
        'seilink' :  seilink
    }
    lst = [1,2,3,4,5,6,7,8,9,10]
    print(seititle)

    return render(request,'seijobs.html',seimens) 

def ltijobs(request):
    mail = request.session['name']
    print(mail)
    with connection.cursor() as cursor:
        query="Select filepath from signupuser where umail = %s"
        cursor.execute(query,[mail])
        filepath = cursor.fetchall()
    # print(type(filepath))
    # print(filepath[0])
    fp = str(filepath[0])
    fp = fp.replace('(','')
    
    fp = fp.replace("'",'')
    fp = fp.replace(',','')
    fp = fp.replace(')','')
    # print(fp)
    domain = skillExtract(fp)
    waldom = domain[-1]
    capedom = domain[0]
    wipdom = domain[1]
    ltidom = capedom
    seimendom = wipdom
    # print(capedom)
    if capedom == "Android+Developer":
        capedom = "Java+Developer"

    ltititle , ltiloc , ltilink = ltijb(waldom)
    lti = {
        'ltititle':ltititle,
        'ltiloc' : ltiloc,
        'ltilink' :  ltilink
    }
    lst = [1,2,3,4,5,6,7,8,9,10]
    # print(ltititle)

    return render(request,'ltijobs.html',lti)  

# def jobsRec(request):
    
    # domain = skillExtract("media\ShumeelMomin_MechEng.pdf")
    # waldom = domain[-1]
    # capedom = domain[0]
    # wipdom = domain[1]
    # ltidom = capedom
    # seimendom = wipdom
    # print(capedom)
    # if capedom == "Android+Developer":
    #     capedom = "Java+Developer"
    # wiptitle , wiploc , wiplink = wipJb(wipdom)
    # littitle , ltiloc , ltilink = ltijb(ltidom)
    # waltitle , walloc , wallink = walmartJb(waldom)
    # seititle , seiloc , seilink = seimensjob(seimendom)
    # wipro = {
    #     'wiptitle':wiptitle,
    #     'wiploc' : wiploc,
    #     'wiplink' :  wiplink
    # }
#     lti = {
#         'littitle':littitle,
#         'ltiloc':ltiloc,
#         'ltilink':ltilink
#     }
#     walmart = {
#         'waltitle':waltitle,
#         'walloc':walloc,
#         'wallink':wallink
#     }
#     seimens ={
#         'seititle':seititle,
#         'seiloc':seiloc,
#         'seilink':seilink
#     }
#     return render(request,'recjobs.html',wipro,lti,walmart,seimens)

def recsignup(request):
    if request.method=='POST':
        
        if request.POST.get('email') and request.POST.get('phone'):
            name = request.POST['username']
            position = request.POST['position']
            phone = request.POST['phone']
            email = request.POST['email']
            pwd = request.POST['password']
            with connection.cursor() as cursor:
                query="Select * from recaccount where email=%s and phone=%s"
                cursor.execute(query,[email,phone])
                row = cursor.fetchall()
                print(len(row))
                if len(row)==1:
                    
                    print("Done Login !!!")
                    request.session['email'] = email
                    request.session['username'] = name
                        # print(filepath)
                    return render(request,'upload.html')
                else:
                    query = "INSERT INTO `recaccount`( name, position , phone , email ,pwd) VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(query,[name ,position,phone,email,pwd])
                    print("Done Registration !!!")
                    request.session['email'] = email
                    request.session['username'] = name
                    return render(request,'upload.html')

def recaccount(request):
    if request.method=='POST':
        if request.POST.get('email') and request.POST.get('password') :
            name = request.POST['username']
            email = request.POST['email']
            pwd = request.POST['password']
            print(name)
            
            with connection.cursor() as cursor:
                query="Select * from recaccount where name = %s and email=%s and pwd=%s"
                cursor.execute(query,[name,email,pwd])
                row = cursor.fetchall()
                print(len(row))
                if len(row)==1:
                    
                    print("Done Login !!!")
                    request.session['email'] = email
                    request.session['username'] = name
                        # print(filepath)
                    return render(request,'upload.html')
                else:
                    return render(request,'HRlogin.html')
from django.utils.datastructures import MultiValueDictKeyError

def matching(request):
    name = request.session['username']
    email = request.session['email']
    if request.method == 'POST' :
        try:
            jobpost = request.POST['document']
            for x in request.FILES.getlist("resumes"):
                print("IM Here !!!!!!!!!!!!")
                def process(f):
                    filepath = initialdir+'/media/files'
                    with open(filepath + str(f),'wb+') as destination:
                        for chunck in f.chuncks():
                            destination.write(chuck)
                process(x)
                print(x)
        except MultiValueDictKeyError:
            jobpost = False
        
        print(jobpost)
        return render(request,'upload.html')


cv = CountVectorizer()
def addfiles(request):
    def extract_text_from_pdf(pdf_path):
        return extract_text(pdf_path)
    def sort_dict_by_value(d, reverse = False):
        return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

    if request.method == 'POST':
        jobpost = request.FILES.get('document')
        resume = request.FILES.getlist('resumes')
        print(resume[0])
        print(resume[-1])
        last = resume.index(resume[-1])
        print(last)
        filename = []
        for i in range(last+1):
            filename.append(resume[i])
        print(filename)
        post = " "
        for x in jobpost:
            post += str(x)
            #print(x)
        post = post.replace("\r"," ")
        post = post.replace('\n'," ")
        post = post.replace("b'"," ")
        # print(post)
        
        # matched = {}
               
        # for x in resume:
        #     for i in x:
        #         #print(i)
        #         i = i.decode('UTF-8')  
        #         print(i)
        #     print("-------")         
        #     filename = f
        #     text = [f,post]
        #     count_matrix = cv.fit_transform(text)
          
        #     matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        #     matchPercentage = round(matchPercentage, 2) 
           
        #     matched[filename] = matchPercentage

        #     print(sort_dict_by_value(matched, True))

        return redirect('dummy')

  
    return render(request, 'upload.html')

def dummy(request):
    return render(request,'index.html')