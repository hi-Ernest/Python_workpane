# coding: utf-8

from wxpy import *
import re

bot = Bot()

# found = bot.friends().search("菠萝油",sex=1)

my_friend = bot.friends().search('lllwww', sex=MALE)[0]
# <Friend: bb>
# 在找到好友(或其他聊天对象)后，还可使用该聊天对象的 send 系列方法，对其发送消息:
# 发送文本
my_friend.send('Hello, WeChat!')

# friend = ensure_one(my_friend)

bf_rules = {
    r'^.*在[吗|嘛]': '在呀，在想你',
    r"^.+[什么|怎么]安排": "都听你的呀,嘻嘻",
    r"^.*代码": "我想了想，不然我们还是分手吧"
}


@bot.register([my_friend, bot.self], msg_types=TEXT, except_self=True)
def reply_bf(msg):
    for rule in bf_rules:
        if re.match(rule, msg.text):
            try:
                # 尝试向消息发送者回复信息
                msg.sender.send_msg(bf_rules[rule])
            except ResponseError as e:
                print (e.err_code, e.err_msg)  # 查看错误号和错误信息
            return
    return "我有点不明白，能不能迁就我一下，我们说点别的吧？"


# 进入python 命令行，让程序保持运行
embed()
