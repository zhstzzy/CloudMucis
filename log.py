from datetime import datetime


class Log:
    def __init__(self):
        now = datetime.now()
        self.msg = ""

    def info(self, msg: str):
        self.msg +="\n" + msg

    def end(self, msg: str):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{now_time}------- {msg}",end="")
        print(self.msg)
