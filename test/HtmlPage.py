# from pip._vendor import requests
# from bs4 import BeautifulSoup
#
# url = "https://wenku.baidu.com/view/9ed32f7ea66e58fafab069dc5022aaea998f41da.html?tdsourcetag=s_pctim_aiomsg&qq-pf-to=pcqq.c2c"
# html = requests.get(url).text
#
# bs = BeautifulSoup(html)
#
# users = bs.select('.c-author')
# for each in users:
#     print(each.text)
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("https://wenku.baidu.com/view/9ed32f7ea66e58fafab069dc5022aaea998f41da.html?tdsourcetag=s_pctim_aiomsg&qq-pf-to=pcqq.c2c/")

reg = '<a class="title" target="_blank" href="(.*?)">(.*?)</a>[\n][\s]*'
reg += '<p class="abstract">[\n](.*)[\n][\s]*'
reg += '</p>[\n][\s]*<div class="meta">[\n][\s]*'
reg += '<a class="collection-tag" target="_blank" href="/c/.*?">(.*?)</a>[\n][\s]*'
reg += '<a target="_blank" href="/p/.*?">[\n][\s]*'
reg += '<i class="iconfont ic-list-read"></i> (.*)[\n]'
reg += '</a>[\s]*<a target="_blank" href="/p/.*?">[\n][\s]*'
reg += '<i class="iconfont ic-list-comments"></i> (.*)[\n]'
reg += '</a>[\s]*<span><i class="iconfont ic-list-like"></i> (.*)</span>[\n][\s]*'
reg += '<span><i class="iconfont ic-list-money"></i> (.*)</span>'

page = re.compile(reg)
artlist = re.findall(page,html)

for arts in artlist:
    for art in arts:
       if art.startswith("/p/"):
         print "http://www.jianshu.com" + art
       else:
           print art