import uiautomator2 as u2
import time
import json

user_info = json.loads(open("user_info.json", "r", encoding="utf-8").read())

d = u2.connect() # connect to device

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

def join_meet():
    push_btn("Join meeting")

def fill_info():
    fill_edit_text("Meeting number or URL", user_info["url"])
    fill_edit_text("Your name", user_info["name"])
    fill_edit_text("Email address", user_info["email"])

def join_room():
    push_btn("JOIN")
    time.sleep(10)
    push_btn("Join")

fill_info()
join_meet()
join_room()