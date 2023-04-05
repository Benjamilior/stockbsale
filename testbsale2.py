import requests
import json
import datetime

# from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account



url = "https://api.bsale.cl/v1/stocks.json" #Url de Acesso 
datos = '6cc26c07ec782ca618620c30c1e7afdeab5b165a.json'#Token de Acesso

headers = {
               'Content-Type': 'application/json',
               "access_token":"6cc26c07ec782ca618620c30c1e7afdeab5b165a"
               }
   #SKU
params2={
      'code':"100143",
      'limit': 2
      }
   #Peticion a la API
response = requests.get(url=url, headers=headers, params=params2)
json_response = response.json()

   #Sacar la cantidad de stock 
for item in json_response['items']:
   quantity = item['quantity']
   print(quantity)
      
   # Sacar fecha de extraccion
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"":now_str}

json_data = json.dumps(data)




SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'abc.json'
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

SPREADSHEET_ID = '1CHkQo1hxYcy1kJgQNHuQxDQIWldZIachwPv08nU84FE'

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()





#Valores a pasar
values = [['100143',quantity,json_data]]
result=sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                             range='A1',
                             valueInputOption='USER_ENTERED',
                                body={'values':values}).execute()
