from datetime import datetime
import requests

class Pushplus:
    def __init__(self, push_token=None):
        now = datetime.now()
        self.msg = now.strftime("%Y/%m/%d (%A) %H:%M:%S")
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.token = push_token
        self.url = "http://www.pushplus.plus/send"

    def end(self, msg: str):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headers = {"Content-Type": "application/json"}
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.info(msg)
        print(f"{now_time}------- {msg}")
        data = {"token": self.token, "title": "音乐合伙人评分"+ msg, "content": self.msg, "template": "txt"}
        data = str(data).encode("utf-8")
        res = requests.session().post(url=self.url, headers=headers, data=data).json()
        print(f"{now_time}--- pushplus {res['msg']}")
        print("= = = = = = = = = = = = = = = = = =")


    def info(self, msg: str):
        self.msg += "\n" + msg
