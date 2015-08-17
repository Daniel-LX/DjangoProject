from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.shortcuts import render_to_response
import collections
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.views.generic import View
from django.shortcuts import render_to_response, redirect
from authentication.models import Authentication_information
import datetime, pytz, requests, time
from django.views.decorators.csrf import csrf_exempt


class ListUsersAuthorize(View):
    def get(self, request):
        code = request.GET.get('code')

        auth_model_information = Authentication_information()

        authorize_to_drchrono(code,auth_model_information)

        return redirect("doctorCheck/")

def post(self):
    return render_to_response('start.html', {'connect': requests.post("https://www.drchrono.com/o/authorize/",params = {
    'redirect_uri' : 'http://127.0.0.1:8000/Hackathon',
    'response_type' : 'code',
    'client_id' : 'UJsvok95ze2mxZc61PlPe8EJML5DRDnCLh7rfLHK',
    'scope' : 'user patients calendar patients:summary',
}).url})


def authorize_to_drchrono(code, auth_model_information):
    data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:8000/Hackathon',
        'client_id': 'UJsvok95ze2mxZc61PlPe8EJML5DRDnCLh7rfLHK',
        'client_secret': 'TuHwE7Ad4T9sudP3xiRI4EZ4yyf5Qdi21dTOBNiL8CpL8zMxbnlJnMnu286on41X2nyiBWUkO4buURohhTSrl4McOYV9BBl7HigDvqPoe6NJctH1E0te57xgC32Ka246',
    }

    response = requests.post('https://www.drchrono.com/o/token/', data)
    response.raise_for_status()
    data = response.json()

    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

    auth_model_information.access_token = access_token
    auth_model_information.refresh_token = refresh_token
    auth_model_information.expiration_date = int(expires_timestamp.strftime("%s"))
    auth_model_information.save()

def refresh_tokens(refresh_token,auth_model_information):
    data={
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
        'client_id': 'UJsvok95ze2mxZc61PlPe8EJML5DRDnCLh7rfLHK',
        'client_secret': 'TuHwE7Ad4T9sudP3xiRI4EZ4yyf5Qdi21dTOBNiL8CpL8zMxbnlJnMnu286on41X2nyiBWUkO4buURohhTSrl4McOYV9BBl7HigDvqPoe6NJctH1E0te57xgC32Ka246',
    }

    return authorize_to_drchrono(data, auth_model_information)


def get_access_tokens():
    my_tokens = Authentication_information.objects.last()

    access_token = my_tokens.access_token
    refresh_token = my_tokens.refresh_token
    expiration_date = my_tokens.expiration_date

    if time.time() >= expiration_date:
        refresh_tokens(refresh_token, my_tokens)
        my_tokens.refresh_from_db()

    access_token = my_tokens.access_token

    return access_token

