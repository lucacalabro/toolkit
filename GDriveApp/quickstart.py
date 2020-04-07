#Script da eseguore stand-alone.
#Trova le credenziali nel file client_secrets_json locato nella stessa directory
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()

gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.




from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)


file_path = "static/upload/trazioniallasbarraprogramma.png"
file1 = drive.CreateFile(metadata={"title": "trazioniallasbarraprogramma.png"})
file1.SetContentFile(file_path)
file1.Upload()


# file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString('Hello World!') # Set content of the file from given string.
# file1.Upload()


# # Auto-iterate through all files that matches this query
# file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# for file1 in file_list:
#   print('title: %s, id: %s' % (file1['title'], file1['id']))