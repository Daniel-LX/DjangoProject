from django.shortcuts import render
import datetime, pytz, requests
from django.views.generic import View
from django.shortcuts import render_to_response,render,HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
class SendEmail(View):
     def post(self,request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email','')
        send_mail(
                subject,
                message,
                'xulu90@yahoo.com',
                [email],
                fail_silently=True)
        return HttpResponseRedirect('/doctorCheck')

     def get(self,request):
          pass

