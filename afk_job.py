import uiautomator2 as u2
import time
import json
import requests
import os
import subprocess

user_info = json.loads(open("user_info.json", "r", encoding="utf-8").read())
print("[start adb connection]")
while True:
    try:
        res = subprocess.check_output(["/usr/bin/adb", "connect", "redroid:5555"])
        if res.find(b"Connection refused") != -1:
            print("[adb connection failed retried]")
            time.sleep(0.5)
            continue

        print("[adb connection success]")
        break
    except subprocess.CalledProcessError:
        print("[adb connection failed retried]")
        time.sleep(0.5)

os.system("poetry run python3 -m uiautomator2 init && adb shell pm grant com.github.uiautomator android.permission.READ_PHONE_STATE")
d = u2.connect("redroid:5555") # connect to device


def fill_edit_text(desc:str, txt:str):
    if d(className="android.widget.EditText", text=desc).exists():
        d(className="android.widget.EditText", text=desc).set_text(txt)
    else:
        raise Exception(f"can not find EditText with desc {desc}")

def push_btn(desc:str):
    if d(className="android.widget.Button", text=desc).exists():
        d(className="android.widget.Button", text=desc).click()
        time.sleep(1)
    else:
        raise Exception(f"can not find Button with desc {desc}")




d.app_start("com.github.uiautomator")
time.sleep(2)
os.system("adb shell input tap 100 450") # dirty hack for enable uiautomator
time.sleep(2)
d.app_uninstall("com.cisco.webex.meetings")
d.app_install("./uc.apk")

d.app_start("com.cisco.webex.meetings")


def join_meet():
    push_btn("Join meeting")

def fill_info():
    fill_edit_text("Meeting number or URL", user_info["url"])
    d.press("back")
    fill_edit_text("Your name", user_info["name"])
    d.press("back")
    fill_edit_text("Email address", user_info["email"])

def join_room():
    push_btn("JOIN")
    time.sleep(10)
    push_btn("Join")


def accept_term_of_use():
    push_btn("ACCEPT")

print("[entering term of use ...]")
while True:
    try:
        accept_term_of_use()
        break
    except Exception as e:
        time.sleep(1)
        print("object does not detected, waiting...")
        print(str(e))

print("[press join meet btn]")
while True:
    try:
        join_meet()
        break
    except Exception:
        # possible jump out update avaible
        d.press("back")

print("[filling personal info]")
while True:
    try:
        fill_info()
        break
    except Exception:
        # possible jump out update avaible
        d.press("back")

print("[entering room]")
while True:
    try:
        join_room()
        break
    except Exception:
        # possible jump out update avaible
        d.press("back")

if "dc_webhook" in user_info:
    d.screenshot("home.jpg")
    requests.post(user_info["dc_webhook"], files={"content":open("home.jpg", "rb")})
