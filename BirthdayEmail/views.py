from django.views.generic import View
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
import datetime, pytz, requests
from django.core.context_processors import csrf

from authentication.views import get_access_tokens
from help_function import getPatientsListByDoctorID,getDoctorList,getPatientsList,list_patients
# Create your views here.

class DoctorCheck(View):
    def get(self,request):
        doctorID = getDoctorList(request)[0]['id']
        args = list_patients(request,doctorID)
        return render_to_response('doctorCheckBirth.html',args)

    def post(self,request):
        doctorID = int(request.POST.get('doctorInput'))
        args = list_patients(request,doctorID)
        return render(request,'doctorCheckBirth.html',args)

class BirthEmail(View):
    def post(self,request):
        patientEmail = request.POST.get('paitentInput')
        return render_to_response('BirthEmail.html',{'email':patientEmail})

    def get(self):
        pass

