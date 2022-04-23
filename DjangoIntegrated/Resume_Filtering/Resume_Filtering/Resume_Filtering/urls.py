"""Resume_Filtering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Resume_Filtering import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path('resumes/',views.resumeupload,name="resumeupload"),
    path('recruiter/',views.recruitersignup,name="recruiter"),
    path('recruiter/reclogin',views.recruiterlogin,name='reclogin'),

    path('logincheck/',views.logincheck,name='logincheck'),
    path('logincheck/logout/', views.logout_view, name='logout'),
    path('logincheck/wipjobs/',views.wipjobs,name = 'wipjobs'),
    path('logincheck/waljobs',views.waljobs,name = 'waljobs'),
    path('logincheck/seijobs',views.seijobs,name = 'seijobs'),
    path('logincheck/ltijobs',views.ltijobs,name = 'ltijobs'),
    path('recaccount',views.recaccount,name = 'recaccount'),
    path('recsignup/',views.recsignup, name= 'recsignup'),
    path('addfiles/',views.addfiles, name= 'addfiles'),
    path('resumes/',views.resumes,name = 'resumes'),
    path('dummy/',views.dummy,name = 'dummy'),

   

]
    


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    