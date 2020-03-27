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



# destinatari può essere una lista o una singola stringa di email
# body è il corpo della email in html
def f(destinatari, soggetto, body):
    import smtplib
    # contenuto = f'From: From Person Subject: {soggetto}\n\n{body}'
    contenuto = f"""From: From Person
        To: To Person
        MIME-Version: 1.0
        Content-type: text/html
        Subject: {soggetto}

        {body}
        """

    mail = smtplib.SMTP('smtp.gmail.com', 587)  # questa configurazione funziona per gmail
    mail.ehlo()  # protocollo per extended SMTP
    mail.starttls()  # email criptata
    mail.login("serviziwebsi@unimib.it", "?sciliam*15")
    mail.sendmail('serviziwebsi@unimib.it', destinatari, contenuto)
    mail.close()



