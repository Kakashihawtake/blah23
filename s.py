import requests
import json

tokens = open("tokens.txt", 'r').read()
url = "https://www.clubhouseapi.com/api/share_channel"


data = json.dumps({
  "channel": input ("Enter your Room code: "),
  "message":input("Enter your Message: ")
})







tokens = tokens.split('\n')

for token in tokens:
    header = {
'CH-Languages': 'en-US',
'CH-Locale': 'en_US',
'Accept': 'application/json',
'Accept-Encoding': 'gzip, deflate',
'CH-AppBuild': '588',
'CH-AppVersion': '1.0.10',
'CH-UserID': '667493545',
'User-Agent': 'clubhouse/588 (iPhone; iOS 15; Scale/2.00)',
'Connection': 'close',
'Content-Type': 'application/json; charset=utf-8',
'Authorization': f"Token {token}"
    }



    response = requests.request("POST",url, headers=header, data=data)
    print(response.status_code)