__author__ = 'root'
# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
import Queue
import os
import re


def getHtml(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    doc = urllib2.urlopen(request, timeout=45).read().decode('utf8')
    return doc

seed = 'http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml'
# seed = 'http://www.xinfadi.com.cn/marketanalysis/0/list/5.shtml'
que_urls = Queue.Queue()
que_urls.put(seed)

myf = open('data_xfd_price.txt', 'w')
p = re.compile('(\d+)\.shtml')

while que_urls.qsize() > 0:
    url = que_urls.get()
    html = getHtml(url)
    dom = etree.HTML(html)
    trs = dom.xpath("//table[@class='hq_table']/tr")
#    print len(trs)

    for tr in trs[1:]:
        try:
            tds = tr.xpath("./td")
            row = [td.text.encode('utf-8') for td in tds[0:-1]]
            line = ' '.join(row)
            myf.write(line + os.linesep)
#            print line
        except AttributeError, e:
            xmlstr = etree.tostring(tr, pretty_print=True)
            print xmlstr
            print e

    myf.flush()

    links = dom.xpath(u"//div[@class='manu']/a[text()=' 下一页 ']/@href")
    for lk in links:
        match = p.search(lk)
        print match.group(1)
        outlink = 'http://www.xinfadi.com.cn' + lk
        print outlink
        que_urls.put(outlink)

myf.close()

