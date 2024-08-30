# 网易云音乐 音乐合伙人脚本

**不是“网易音乐人”的脚本呐！！！**

## 🔥 功能

[手动](#-本地手动运行)配合cron实现自动完成**音乐合伙人**任务。

(可选) 使用[钉钉机器人](https://open.dingtalk.com/document/robots/custom-robot-access/)
或[pushplus（推送加）](https://www.pushplus.plus/)返回任务完成情况。

## 📖 使用说明

### 💻 本地手动运行

1. 下载 "main.py", "Pushplus.py",Dingtalk.py, "setting_default.yml", **需放到同一文件夹内**
2. 填写"setting_default.yml"，[参数说明](#-参数说明)
3. 直接执行"main.py"

### ⚙ 参数说明

#### 网易云参数

| 参数名     | 说明          | 获取                              |
|:--------|:------------|:--------------------------------|
| MUSIC_U | 网易云音乐cookie | [网易云音乐](https://music.163.com/) |
| __csrf  | 网易云音乐cookie | [网易云音乐](https://music.163.com/) |

#### push-plus推送参数 [pushplus(推送加)-破壳网络科技旗下微信消息推送平台](https://www.pushplus.plus/)

| 参数名    | 说明         | 获取         |
|:-------|:-----------|:-----------|
| enable | 是否开启推送     | true/false |
| token  | 发送推送的token | 上面官网获取     |

#### 钉钉机器人参数 [钉钉机器人](https://open.dingtalk.com/document/robots/custom-robot-access/)

| 参数名    | 说明         | 获取         |
|:-------|:-----------|:-----------|
| enable | 是否开启推送     | true/false |
| token  | 发送推送的token | 钉钉群中自定义机器人 |
| secret | 发送推送的安全设置  | 钉钉群中自定义机器人 |

#### telegram 机器人推送 [telegram机器人](https://core.telegram.org/bots)

| 参数名    | 说明           | 获取         |
|:-------|:-------------|:-----------|
| enable | 是否开启推送       | true/false |
| token  | 发送推送的token   | 上面官网获取     |
| chat_id | 发送推送的chat_id | 上面官网获取     |
| proxy | 代理           | 自行设置       |

- 用户的chat_id 如何获取
  使用以下代码创建一个 Telegram bot 并发送一条消息：

  ``````python
  import telegram
  
  bot_token = 'YOUR_BOT_TOKEN'
  chat_id = 'YOUR_CHAT_ID'
  bot = telegram.Bot(token=bot_token)
  bot.send_message(chat_id=chat_id, text='Hello, World!')
  ``````

  在上面的代码中，你需要将 YOUR_BOT_TOKEN 替换为你的机器人 token，将 YOUR_CHAT_ID 替换为你想要发送消息的聊天 ID。这里的 chat_id 可以是一个用户的 ID，也可以是一个群组或频道的 ID。
  使用 `bot.send_message()` 函数，可以向指定 chat_id 发送一条消息。你可以根据需要自定义消息的内容和格式。
  如果你需要发送更复杂的消息，例如带有键盘、按钮、图片、文件等的消息，可以使用 Telegram Bot API 的其他方法。可以参考 python-telegram-bot 的文档以了解更多信息。
- 获取群组的 chat_id 可以通过以下步骤：

  1. 首先，将你的 Telegram 机器人添加到群组中。你可以通过搜索机器人的用户名或者将机器人添加到群组中，或者通过分享链接将机器人添加到群组中。
    接下来，向群组发送一条消息。

  2. 打开浏览器，输入以下链接：https://api.telegram.org/bot<YourBOTToken>/getUpdates，其中 <YourBOTToken> 是你的机器人的 token。

  3. 这将返回一个 JSON 格式的响应，其中包含最近一条消息的信息，包括 chat_id。在响应中找到 chat 对象，它包含了群组的 chat_id，格式如下：

    ``````json
    jsonCopy code
    "chat": {
        "id": -1001234567890,
        "title": "Group Name",
        "type": "supergroup"
    },
    ``````


- Cookie两周左右就会过期，请及时更新参数

* 详情见[setting_default.yml](./setting_default.yml)

## 🔈 特别声明

- 本仓库发布的脚本及其中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

- 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

- 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。

- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播,
  本人对于由此引起的任何隐私泄漏或其他后果概不负责。

- 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。

- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。

- 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明。

**您必须在下载后的24小时内从计算机或手机中完全删除以上内容**

> ***您使用或者复制了本仓库且本人制作的任何脚本，则视为 `已接受` 此声明，请仔细阅读***

## 😘 鸣谢

代码参考 & "README"：

- https://github.com/KotoriMinami/qinglong-sign
- https://github.com/C20C01/CloudMusicBot

依赖包：https://github.com/LeonX86/Music-copartner-sverless

