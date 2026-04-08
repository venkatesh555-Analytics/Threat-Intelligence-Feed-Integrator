import requests
import time

VT_API_KEY = "9bfec5898df22164babceabfgtseeae6e673c5b53bcaa43a92d7e6f08e99a1de37f881"
ABUSE_API_KEY = "674b64d2509ac32156791955e3aa9f7465eab09bc1c6e3281a4da8676a78052f1f1d9fe5ccba612ff9a6"

def check_virustotal(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["attributes"]["last_analysis_stats"]["malicious"]
    return "Error"

def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": ABUSE_API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()["data"]["abuseConfidenceScore"]
    return "Error"

with open("ioc_list.txt") as file:
    ips = file.read().splitlines()

print("IP\tVT\tAbuse")

for ip in ips[:50]:
    vt = check_virustotal(ip)
    abuse = check_abuseipdb(ip)

    print(f"{ip}\t{vt}\t{abuse}")

    time.sleep(15)
