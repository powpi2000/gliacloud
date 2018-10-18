# coding=utf-8
from urllib.parse import urlparse
import os
import requests
import lxml
from lxml import etree
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
fd = {}
for url in urls:
    o = urlparse(url)
    f = os.path.basename(o.path)
    if f in fd:
        fd[f] = fd[f] + 1
    else:
        fd[f] = 1
print("p1:")
print(fd)

def anonymous(x):
    return x**2 + 1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        ''' your work here '''
        area = area + anonymous(intercept) * intercept
    return area
print(integrate(anonymous, 0, 10))

total = 0 
for i in range(1000):
    if i%3 ==0 or i %5 ==0:
        total = total + i
print(total)

r = requests.get('https://www.ptt.cc/bbs/NBA/M.1539828006.A.905.html')
#tree = lxml.html.fromstring(html)
html  = r.text
tree = etree.HTML(html)
meta_right = tree.xpath("//div[contains(@class, 'article-metaline-right')]")

data = {}
meta_board = meta_right[0].xpath('.//span/text()')
data['board'] = meta_board[1]

metas = tree.xpath("//div[contains(@class, 'article-metaline')]")
for meta in metas:
    meta_v = meta.xpath('.//span/text()')
    if meta_v[0] == "作者":
        data['author'] = meta_v[1]
    elif meta_v[0]== "標題":
        data['title'] = meta_v[1]
    elif meta_v[0]== "時間":
        data['time'] = meta_v[1]
x_content = tree.xpath("//div[contains(@id, 'main-content')]")
content = etree.tostring(x_content[0], pretty_print=True, method='html').decode("utf-8")
data['content'] = content
print(data)






