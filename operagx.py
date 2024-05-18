import requests
from hashlib import sha256
import uuid
import threading

def loopfunction():
    while True:
        yeah = str(uuid.uuid4())
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        payload = {"partnerUserId": sha256(yeah.encode('utf-8')).hexdigest()}
        headers = {
            "authority": "api.discord.gx.games",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.opera.com",
            "referer": "https://www.opera.com/",
            "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Opera GX\";v=\"106\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        f = open("promourls.txt", "a")
        f.write("https://discord.com/billing/partner-promotions/1180231712274387115/"+response.json().get("token")+"\n")
        f.close()
        print("Generated code using partnerUserId: " + sha256(yeah.encode('utf-8')).hexdigest())

if __name__ =="__main__":
    threadamount = input("How many threads do you want to use? ")
    for i in range(int(threadamount)):
        t = threading.Thread(target=loopfunction)
        t.start()