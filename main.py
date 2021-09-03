import os
import io
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
if os.path.exists('token.json'):
        #creds = service_account.Credentials.from_service_account_file('token.json')
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print(creds.expired)
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("came here")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
service = build('drive', 'v3', credentials=creds)
print("hello")
file_ids = [""]
file_names = ["tanjore"]
for file_id, file_names in zip(file_ids, file_names):
    fh = io.BytesIO
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    print(items)