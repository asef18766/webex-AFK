import uiautomator2 as u2
import time
import json
import requests
import os
import subprocess
import schedule
user_info = json.loads(open("user_info.json", "r", encoding="utf-8").read())

def akf_ensure_success():
    while True:
        try:
            subprocess.run(["/root/.local/bin/poetry", "run", "python3", "afk_job.py"], timeout=120, check=True)
            break
        except subprocess.TimeoutExpired:
            print("[proc timeout retried :P]")
        except subprocess.CalledProcessError:
            print("[proc encounter failure]")
        
getattr(schedule.every(), user_info["day"]).at(user_info["time"], "Asia/Taipei").do(akf_ensure_success)
while True:
    schedule.run_pending()
    time.sleep(1)