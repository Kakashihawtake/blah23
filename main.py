import requests
import threading
channel_id = input("Roomcode: ")





def send_join_room(token):
    BASEURL =    "https://www.clubhouseapi.com:443/api/join_channel"
    headers = {
        "CH-Languages": "en-US",
        "CH-Locale": "en_US",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "CH-AppBuild": "304",
        "CH-AppVersion": "0.1.28",
        "CH-UserID": "119681133",
        "User-Agent": "clubhouse/android/1447",
        "Connection": "keep-alive",
        "Authorization": f"Token {token}"
    }
    data = {"channel": channel_id}
    response = requests.post(BASEURL, data=data, headers=headers)
    try:
                data = response.json()                
    except requests.exceptions.RequestException:
                print(response.text)











# active_ping

def send_online_loop(token):
    while True:
        BASEURL = "https://www.clubhouseapi.com/api/active_ping"
        headers = {
            "CH-Languages": "en-US",
            "CH-Locale": "en_US",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "CH-AppBuild": "304",
            "CH-AppVersion": "0.1.28",
            "CH-UserID": "119681133",
            "User-Agent": "clubhouse/android/1447",
            "Connection": "keep-alive",
            "Authorization": f"Token {token}"
        }
        data = {
            "channel": channel_id
        }
        response = requests.post(BASEURL, data=data, headers=headers)
        try:
                response.raise_for_status()
                print(f"Successfully sent Keep Online in channel {channel_id} with token {token}")               
        except requests.exceptions.RequestException as e:
                print(f"Error sending Keep Online in channel {channel_id} with token {token}: {e}")





















# Create two threads, one for sending Join Room requests and the other for sending Active Ping requests
join_room_threads = []
accept_speaker_invite_threads = []
send_online_loop_threads = []


with open("tokens.txt", "r") as f:
 for line in f:
    token = line.strip()
    join_room_thread = threading.Thread(target=send_join_room, args=(token,))
    send_online_loop_thread = threading.Thread(target=send_online_loop, args=(token,))
    join_room_threads.append(join_room_thread)
    send_online_loop_threads.append(send_online_loop_thread)

# Start the threads
for thread in join_room_threads:
    thread.start()

for thread in send_online_loop_threads:
    thread.start()

# Wait for all threads to finish
for thread in join_room_threads:
    thread.join()

for thread in send_online_loop_threads:
    thread.join()
