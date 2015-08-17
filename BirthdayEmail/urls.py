"""drchronoHackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import DoctorCheck,BirthEmail
from send_Email.views import SendEmail
from authentication.views import post,ListUsersAuthorize

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Hackathon/', ListUsersAuthorize.as_view(), name="list_users_authorize"),
    url(r'^start/$', post),
    url(r'^doctorCheck/',DoctorCheck.as_view(), name="doctorCheck"),
    url(r'^BirthEmail/',BirthEmail.as_view(),name="birthEmail"),
    url(r'^send/$',SendEmail.as_view(),name="sendEmail"),
]
urlpatterns +=staticfiles_urlpatterns()