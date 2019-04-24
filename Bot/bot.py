# coding: utf-8
import json
import requests
from wxpy import *


def reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "7e5e7f3ce4c2449b8f3fe5f9a9407870"
    payload = {
        "key": api_key,
        "info": "text",
        "userid": "666"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    if 'url' in result.keys():
        return "" + result["text"] + result["url"]
    else:
        return "" + result["text"]


bot = Bot(cache_path=True)  # 登录缓存
print('小新上线')
found = bot.friends().search('M')
print(found)


@bot.register(found)
def message(msg):
    ret = reply(msg.text)
    return ret


@bot.register(found)
def forward_message(msg):
    ret = reply(msg.text)
    return ret


embed()
