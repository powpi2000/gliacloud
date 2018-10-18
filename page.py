from urllib.parse import urlparse
import os 
import requests
import lxml
from lxml import etree
import random
r = requests.get('http://wiki.python.org.tw/The%20Zen%20Of%20Python')
#tree = lxml.html.fromstring(html)
html  = r.text
tree = etree.HTML(html)
zens = tree.xpath("//p[contains(@class, 'line874')]/text()")
i = random.randint(0,len(zens))
print("<html><body>{}</bpdy></html>".format(zens[i]))

