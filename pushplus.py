from datetime import datetime
import requests

class pushplus:
    def __init__(self, push_enable, push_token=None):
        now = datetime.now()
        self.msg = now.strftime("%Y/%m/%d (%A) %H:%M:%S")
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.enable = push_enable
        self.token = push_token
        self.url = "http://www.pushplus.plus/send"

    def end(self, msg: str):
        headers = {"Content-Type": "application/json"}
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.info(msg)
        if self.enable == False:
            print(self.msg)
        else:
            data = {"token": self.token, "title": "音乐合伙人评分", "content": self.msg, "template": "txt"}
            data = str(data).encode("utf-8")
            res = requests.session().post(url=self.url, headers=headers, data=data).json()
            now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now_time}--- pushplus {res['msg']}")


    def info(self, msg: str):
        self.msg += "\n" + msg
