from datetime import datetime
from urllib import parse

import requests
import time
import hmac
import hashlib
import base64


class DingTalk:
    def __init__(self, token=None, secret=None):
        # now = datetime.now()
        # self.msg = now.strftime("%Y/%m/%d (%A) %H:%M:%S")
        # self.msg += "\n= = = = = = = = = = = = = = = = = "
        self.msg = ''
        self.secret = secret
        self.token = token

        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        sign = parse.quote_plus(base64.b64encode(hmac_code))

        self.url = 'https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}'.format(self.token,
                                                                                                         timestamp,
                                                                                                         sign)

    def send(self, msg: str):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headers = {"Content-Type": "application/json"}
        self.msg += msg
        print(f"{now_time}------- {msg}")
        text = '# 网易云音乐合伙人评分 \n\r ### 时间 \n\r' + now_time + '\n\r ### 消息 \n\r' + self.msg
        data = {
            # // markdown消息
            "markdown": {
                "text": text,
                "title": '音乐合伙人通知'
            },
            "msgtype": "markdown",

        }
        data = str(data).encode("utf-8")
        res = requests.post(url=self.url, headers=headers, data=data).json()
        if res['errcode'] == 0:
            print(f"{now_time}------- 钉钉消息发送成功")
        else:
            print(f"{now_time}------- 钉钉消息发送失败")


def info(self, msg: str):
    self.msg += msg + '\n\r'
