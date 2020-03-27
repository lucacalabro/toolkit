import re

# Richieste per rest service
import requests
from django.http import JsonResponse
from requests_auth import Basic

# Create your views here.
user = "forms"
passwd = "yg7dpwn0.pdk69gn"

urlStudent = ["https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsStudente/matricola/"
    , "https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsStudente/codFis/"
    , "https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsStudente/emailAte/"]
urlEmployee = ["https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsRu/matricola/"
    , "https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsRu/codFis/"
    , "https://equipe.si.unimib.it/equipe-web/webresources/ActionFormsRu/email/"]


# pip install requests-auth

# I valori restituiti sono liste di dizionari

# http://127.0.0.1:8000/restserviceesse3/studentematricola/735656/
def studentematricola(request, matricola):
    response = requests.get(urlStudent[0] + str(matricola), auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


# http://127.0.0.1:8000/restserviceesse3/studentecodicefiscale/CLBLCU78B03B791H/
def studentecodicefiscale(request, codicefiscale):
    # Se il formato codice fiscale non è corretto solleva eccezione
    if not checkCodFis(codicefiscale):
        raise ValueError("Formato codicefiscale studente errato")

    codicefiscale = codicefiscale.upper()  # Il Cod fis deve essere sempre con tutti i caratteri maiuscoli

    response = requests.get(urlStudent[1] + codicefiscale, auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


# http://127.0.0.1:8000/restserviceesse3/studenteemail/l.calabro2@campus.unimib.it/
def studenteemail(request, email):
    # Se il formato della remail non è corretto solleva eccezione
    if not checkEmail(email):
        raise ValueError("Formato email studente errato")

    response = requests.get(urlStudent[2] + email, auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


# http://127.0.0.1:8000/restserviceesse3/utentematricola/002392/
def utentematricola(request, matricola):
    response = requests.get(urlEmployee[0] + str(matricola), auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


# http://127.0.0.1:8000/restserviceesse3/utentecodicefiscale/CLBLCU78B03B791H/
def utentecodicefiscale(request, codicefiscale):
    # Se il formato codice fiscale non è corretto solleva eccezione
    if not checkCodFis(codicefiscale):
        raise ValueError("Formato codicefiscale utente errato")

    codicefiscale = codicefiscale.upper()  # Il Cod fis deve essere sempre con tutti i caratteri maiuscoli

    response = requests.get(urlEmployee[1] + codicefiscale, auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


# http://127.0.0.1:8000/restserviceesse3/utenteemail/luca.calabro@unimib.it/
def utenteemail(request, email):
    # Se il formato della email non è corretto solleva eccezione
    if not checkEmail(email):
        raise ValueError("Formato email utente errato")

    response = requests.get(urlEmployee[2] + email, auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


def testRest(request):
    response = requests.get(urlEmployee[2] + 'luca.calabro@unimib.it', auth=Basic(user, passwd))

    response_json = response.json()

    return checkList(response_json)


def checkEmail(email):
    """Prende in ingresso una stringa
        e controlla che abbia un formato corretto
        come email

            Parameters:
            email: stringa rappresentante l'email da controllare

            :rtype: bool
           """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if (re.search(regex, email)):
        return True

    else:
        return False


def checkList(response_json_lista):
    """Prende in ingresso una lista JSON
    e la restituisce come JsonResponse se la lunghezza è != 0
    altrimenti restituisce None

        Parameters:
        response_json_lista (<Lista JSON>): Lista JSON REstituita dall'interrogazione del REST serviceESSE3

        Returns:
        <Lista JSON> o None
       """
    if len(response_json_lista) != 0:
        return JsonResponse(response_json_lista, safe=False)
    else:
        return None


def checkCodFis(codicefiscale):
    """Prende in ingresso una stringa
            e controlla che abbia un formato corretto
            come codicefiscale

                Parameters:
                codicefiscale: stringa rappresentante l'email da controllare

                :rtype: bool
               """
    regex = '^[a-zA-Z]{6}[0-9]{2}[abcdehlmprstABCDEHLMPRST]{1}[0-9]{2}([a-zA-Z]{1}[0-9]{3})[a-zA-Z]{1}$'

    if (re.search(regex, codicefiscale)):
        return True

    else:
        return False



