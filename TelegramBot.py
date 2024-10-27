import telegram
from telegram.utils.request import Request
from datetime import datetime


class TelegramBot:
    def __init__(self, bot_token, chat_id, proxy_url='http://127.0.0.1:7890'):
        self.msg = ''
        self.bot_token = bot_token
        self.chat_id = chat_id
        proxy = Request(proxy_url=proxy_url)
        self.bot = telegram.Bot(token=bot_token, request=proxy)

    def send_message(self, message):
        self.bot.send_message(chat_id=self.chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)

    def info(self, msg: str):
        self.msg += msg + '\r\n'

    def send(self, msg: str):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headers = {"Content-Type": "application/json"}
        text = "*网易云音乐合伙人评分*\r\n*=========== 时间 ===========*\r\n {time} \r\n*=========== 消息 ===========*\r\n\r\n {message}"
        data = text.format(time=now_time, message=msg)
        self.send_message(data)
