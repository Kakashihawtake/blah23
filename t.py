import requests
import json

url = "https://www.clubhouseapi.com/api/complete_phone_number_auth"

phone_number = input("Enter your phone number: ")
verification_code = input("Enter the verification code sent to your phone: ")

payload = json.dumps({
  "phone_number": phone_number,
  "verification_code": verification_code
})
headers = {
  "Content-Type": "application/json; charset=utf-8",
  "Content-Length": str(len(payload)),
  "Accept-Encoding": "gzip, deflate",
  "Accept": "application/json",
  "User-Agent": "clubhouse/android/1019808",
  "Ch-Appbuild": "1019808",
  "Ch-Appversion": "23.02.16",
  "Ch-Deviceid": "f3879847-6534-431a-9c32-915c85c8a4c3",
  "Ch-Devicemfr": "Genymobile",
  "Ch-Devicemodel": "Redmi Note 7",
  "Ch-Locale": "[en_US]",
  "Ch-Keyboards": "en-USen-US",
  "Ch-Session-Id": "5ecdfb5d-ff66-4477-a79f-dad5ea66b73e",
  "Accept-Language": "en-US"
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    response_data = response.json()
    auth_token = response_data["auth_token"]
    with open("tokens.txt", "a") as f:
        f.write(auth_token + "\n")
    print("Authentication successful. Token saved in tokens.txt")
else:
    print(f"Authentication failed. Status code: {response.status_code}")