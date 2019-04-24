# import itchat, time, re
# from itchat.content import *
# import urllib2, urllib
# import json
#
#
# @itchat.msg_register([TEXT])
# def text_repy(msg):
#     info = msg['Text'].encode('UTF-8')
#     url = "http://www.tuling123.com/openapi/api"
#     data = {u"key": "7e5e7f3ce4c2449b8f3fe5f9a9407870", "info": info, u"loc": "", "userid": ""}
#     data = urllib.urlencode(data)
#
#     url2 = urllib2.Request(url, data)
#
#     response = urllib2.urlopen(url2)
#
#     apicontent = response.read()
#     s = json.loads(apicontent, encoding='UTF-8')
#     print 's==', s
#     if s['code'] == 100000:
#         itchat.send(s['text'], msg['FromUserName'])
#
#
# itchat.auto_login(enableCmdQR=2, hotReload=True)
# itchat.run(debug=True)


import itchat
from itchat.content import *
import json
import requests


@itchat.msg_register([TEXT])
def text_reply(msg):
    info = msg['Text'].encode('utf-8')
    url = 'http://www.tuling123.com/openapi/api'
    data = {u"key": "7e5e7f3ce4c2449b8f3fe5f9a9407870", "info": info, u"loc": "", "userid": ""}
    response = requests.post(url, data).content
    s = json.loads(response, encoding='utf-8')
    print('s == %s' % s)
    if s['code'] == 100000:
        itchat.send(s['text'], msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run(debug=True)
