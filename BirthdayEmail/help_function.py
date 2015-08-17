from authentication.views import get_access_tokens
from django.core.context_processors import csrf
import datetime, pytz, requests

def getDoctorList(request):
    headers = {
        'Authorization': 'Bearer %s' % (get_access_tokens()),
    }
    doctors = []
    doctors_url = 'https://drchrono.com/api/doctors'
    while doctors_url:
        data = requests.get(doctors_url, headers=headers).json()
        doctors.extend(data['results'])
        doctors_url = data['next']  # A JSON null on the last page
    return doctors

def getPatientsListByDoctorID(doctorID):
    headers = {
        'Authorization': 'Bearer %s' % (get_access_tokens()),
    }
    patients = []
    patients_url = 'https://drchrono.com/api/patients'
    patients_url += "?doctor=%s" % doctorID
    while patients_url:
        data = requests.get(patients_url, headers=headers).json()
        patients.extend(data['results'])
        patients_url = data['next']  # A JSON null on the last page
    return patients

def getPatientsList(request):
    headers = {
        'Authorization': 'Bearer %s' % (get_access_tokens()),
    }
    patients = []
    patients_url = 'https://drchrono.com/api/patients'
    while patients_url:
        data = requests.get(patients_url, headers=headers).json()
        patients.extend(data['results'])
        patients_url = data['next']  # A JSON null on the last page
    return patients

def list_patients(request, DoctorID ):
    now  = datetime.datetime.now()
    doctor = getDoctorList(request)
    patientListByDoctorID = getPatientsListByDoctorID(DoctorID)
    whoIsBirth = []

    for patient in patientListByDoctorID:
        if len(patient['email']) != 0:
            if patient['date_of_birth'] is not None:
                part = patient['date_of_birth'].split('-')
                if now.month == int(part[1]) and now.day == int(part[2]):
                    whoIsBirth.append(patient['id'])

    args = {}
    args.update(csrf(request))
    args['doctors'] = doctor
    args['patientList'] = patientListByDoctorID
    args['whoIsBirth'] = whoIsBirth

    return args
