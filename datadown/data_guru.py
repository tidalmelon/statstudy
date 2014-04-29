# --*-- coding:utf-8 --*--
import urllib2
from lxml import etree
import Queue
import time
import os
# 所有thirft编程都需要的
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
# Ｈbase的 客户端代码
from hbase import ttypes
from hbase.Hbase import Client, ColumnDescriptor, Mutation


class HbaseUtil:
    def __init__(self, tableName, host='localhost', port=9090):
        self.tableName = tableName
        transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Client(protocol)
        self.transport.open()
        if tableName not in self.client.getTableNames():
            print 'creating table %s' % tableName
            columns = []
            col = ColumnDescriptor()
            col.name = 'page:title'
            col.maxVersions = 10
            columns.append(col)
            col = ColumnDescriptor()
            col.name = 'page:article'
            columns.append(col)
            self.client.createTable(tableName, columns)
        #self.printAll()

    def close(self):
        self.transport.close()

    def insert(self, rowkey, title, content):
        mutations = [Mutation(column='page:article', value=content.encode('utf-8')),
                     Mutation(column='page:title', value=title.encode('utf-8'))]
        self.client.mutateRow(self.tableName, rowkey, mutations, {})

    def existRowKey(self, rowkey):
        pass

    def printAll(self):
        print 'starting scanner...'
        scanner = self.client.scannerOpen(self.tableName, '', ['page:title'], {})
        r = self.client.scannerGet(scanner)
        while r:
            for i in r:
                print i.row
                for k, v in i.columns.items():
                    print k, v.value, v.timestamp
                    x = v.value
                    print x
            r = self.client.scannerGet(scanner)
        print 'scanner finished '


def getHtml(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    doc = urllib2.urlopen(request, timeout=45).read().decode('gbk')
    return doc


seed = 'http://it.dataguru.cn/'
# seed = 'http://bi.dataguru.cn/'
# seed = 'http://science.dataguru.cn/'
que_urls = Queue.Queue()
que_urls.put(seed)


def getCurTimeStamp(root='/data/data/dataguru/science/'):
    """
    获取当前时间戳：离1970年1月1日午夜开始的毫秒数
    :return:
    """
    return root + str(int(time.time() * 1000)) + '.txt'


def start():
    # connect to hbase and open
    db = HbaseUtil('webpage')

    while que_urls.qsize() > 0:
        url = que_urls.get()
        html = getHtml(url)
        dom = etree.HTML(html)
        links = dom.xpath(u"//div[@id='ct']//a[@class='xi2']")
        print len(links)
        for lk in links:
            print lk.text, lk.xpath('./@href')
            try:
                link = lk.xpath('./@href')[0]
                html_c = getHtml(link)
                dom_c = etree.HTML(html_c)
                article = dom_c.xpath('//td[@id="article_content"]//text()')
                content = os.linesep.join(article)
                content = content.replace('\r\n', '')

                # write to hbase
                db.insert(link, lk.text, content)

                # write to filesystem
                # with open(getCurTimeStamp(), 'wb') as mf:
                #     mf.write(link + os.linesep)
                #     mf.write(lk.text.encode('utf-8') + os.linesep)
                #     mf.write(content.encode('utf-8'))
            except Exception, e:
                print e
                continue

        links_next = dom.xpath('//div[@id="ct"]//a[@class="nxt"]')
        for lk in links_next:
            print lk.text, lk.xpath('./@href')
            que_urls.put(lk.xpath('./@href')[0])
    # close hbase connection
    db.close()

# import jieba
if __name__ == '__main__':
    start()
    # sen = '我来到北京清华大学'
    # sen = '他来到了网易杭研大厦'
    # seg_list = jieba.cut(sen, cut_all=False)
    # res = "/ ".join(seg_list)
    # print type(seg_list)
    # print "Default Mode:", "/ ".join(seg_list)  # 精确模式