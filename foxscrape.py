# Modules
import os, time, queue, threading
import pandas as pd 
import requests
from banner import *

# Variables Setup
q = queue.Queue()
threads = []
valid_proxies = []
temp_p = []

def scraping():
    # Scraping
    print(f"{BLUE}[-]Starting Scraping...")
    u = "https://free-proxy-list.net"
    p = pd.read_html(u)[0]
    
    # Filtering
    print(f"{BLUE}[-]Filtering...")
    f = p.loc[
        (p['Anonymity'] == 'elite proxy') &
        (p['Https'] == 'yes')
        ]
    h = p['IP Address'].astype(str) +':'+ p['Port'].astype(str)
    
    # Creating
    print(f"{BLUE}[-]Capturing...")
    proxy = h.tolist()
    with open("tempprox.txt",'w')as f:
        for p in proxy:
            f.write(p + '\n')
 
def check_proxies():
    while not q.empty():
        proxy = q.get()
        try:
            # Test the proxy
            res = requests.get("https://ipinfo.io/json", 
                              proxies={"http": proxy, "https": proxy},timeout=5
                              )
            if res.status_code == 200:
                print(f"{BOLD}{GREEN}[✓]Active: {proxy}")
                valid_proxies.append(proxy)
        except:
             continue
        finally:
            q.task_done()

# Start
banner()
scraping()
time.sleep(1)

# Sorting Proxies
print(f"{BLUE}[-]Sorting Proxies...")
if os.path.exists("tempprox.txt"):
    os.system("cat tempprox.txt | sort -u > temp.txt")

# Read proxies from tempprox.txt
with open("temp.txt", "r") as f:
    proxies = [p.strip() for p in f.readlines() if p.strip()]
    for p in proxies:
        q.put(p)
        temp_p.append(p)

# Printing Sorted Proxies
print(f"{GREEN}[✓]{len(temp_p)} Scraped Proxies")

# Checking Proxies
print(f"{BLUE}[-]Validating Process...\n")
for _ in range(20):  # Reduced to 20 threads
    t = threading.Thread(target=check_proxies)
    t.start()
    threads.append(t)

# Wait for all proxies to be checked
q.join()

# Printing How many Proxies working.
print(f"\n{GREEN}[✓]{len(valid_proxies)} Working Proxies")

# Saving Valid Proxies file
print(f"{BLUE}[-]Creating file...")
with open("output.txt", "a") as f:
    for p in valid_proxies:
        f.write(p + "\n")
print(f"{GREEN}[✓]Proxies file created successfully.")

#Cleaning
print(f"{BLUE}[-]Cleaning...")
if os.path.exists("tempprox.txt") and os.path.exists("temp.txt"):
    os.remove("tempprox.txt")
    os.remove("temp.txt")
print(f"{GREEN}[✓]Cleaning Completed")

#Finish
print(f"{GREEN}[✓]Done"\n)