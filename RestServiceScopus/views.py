from json.decoder import JSONDecodeError

# Richieste per rest service
import requests
from django.http import JsonResponse

# Create your views here.


# https://api.crossref.org/works/10.1016/0197-2456(96)84672-1
# http://127.0.0.1:8000/restservicescopus/scopusrequestbydoi/10.1016/0197-2456(96)84672-1/
urlScopus = ["https://api.crossref.org/works/"]


def scopusrequestbydoi(request, doi):
    try:
        response = requests.get(urlScopus[0] + doi)
        response_json = response.json()
    except JSONDecodeError:
        # print("DOI ERRATO")
        return None
        # HttpResponse("DOI ERRATO")
    else:
        return JsonResponse(response_json, safe=False)

