# emailsender("Soggetto email", "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>", [], ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it'],['calabroluca78@gmail.com', 'lucalalabro78@live.com'])
# emailsender("Soggetto email", "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>", ['lucalalabro78@gmail.com'], ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it'],['calabroluca78@gmail.com', 'lucalalabro78@live.com'])
def emailsender(subject, body, listTO, listCC, listBCC):
    # documentazione consultata
    # https://stackoverflow.com/questions/1546367/python-how-to-send-mail-with-to-cc-and-bcc
    # https://docs.python.org/3/library/email.examples.html
    import smtplib

    # Import the email modules we'll need
    from email.message import EmailMessage

    msg = EmailMessage()
    msg.add_header('Content-Type', 'text/html')

    email_content = f"<html><head></head><body>{body}</body></html>"
    msg.set_payload(email_content)
    # msg.set_content(email_content)

    msg['Subject'] = subject
    # msg['From'] = "serviziwebsi@unimib.it"
    msg['From'] = "noreplay@unimib.it"
    msg['To'] = ', '.join(listTO)
    msg['Cc'] = ', '.join(listCC)
    msg['Bcc'] = ', '.join(listBCC)

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()  # protocollo per extended SMTP
    s.starttls()
    s.login("serviziwebsi@unimib.it", "?sciliam*15")
    s.send_message(msg)
    s.quit()

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# # sendemail("Soggetto email", "<h1>Titolo</h1><p>paragrafo1</p><p>paragrafo2</p>", "lucalalabro78@gmail.com", "luca.calabro@unimib.it")
# # subject: soggetto email
# # *lista destinatari bcc: tupla di strighe composte da indirizzzi email es: a@a.it, b@b.it o (a@a.it, b@b.it)
# # body: corpo in formato html
# # From: Campo nell'header della email () sembra non avere peso,  si può eventualemtne lasciare vuoto
# # To: Campo nell'header della email, si può eventualemtne lasciare vuoto
# def sendemail(subject, body, To, From, *lista_destinatari):
#     # Create message container - the correct MIME type is multipart/alternative.
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = From
#     msg['To'] = To
#
#     # Create the body of the message (a plain-text and an HTML version).
#     # text = "{body}" #Per inviare come plain tect
#
#     html = f"""\
#     <html>
#       <head></head>
#       <body>
#         {body}
#       </body>
#     </html>
#     """
#
#     # Record the MIME types of both parts - text/plain and text/html.
#
#     # part1 = MIMEText(text, 'plain') #Per inviare come plain text
#     part2 = MIMEText(html, 'html')  # Per inviare come email
#
#     # Attach parts into message container.
#     # According to RFC 2046, the last part of a multipart message, in this case
#     # the HTML message, is best and preferred.
#
#     # msg.attach(part1) #Per inviare come plain text
#     msg.attach(part2)  # Per inviare come email
#
#     # Send the message via local SMTP server.
#     s = smtplib.SMTP('smtp.gmail.com', 587)  # questa configurazione funziona per gmail
#     s.ehlo()  # protocollo per extended SMTP
#     s.starttls()  # email criptata
#     s.login("serviziwebsi@unimib.it", "?sciliam*15")
#     s.sendmail("", lista_destinatari, msg.as_string())  # SEMBRA CHE IL PRIMO PARAMETRO NON ABBIA PESO
#     s.quit()
