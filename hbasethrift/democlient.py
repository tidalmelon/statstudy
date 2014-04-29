# --*-- coding:utf-8 --*--

import sys
import time

# 所有thirft编程都需要的
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
# Ｈbase的 客户端代码
from hbase import ttypes
from hbase.Hbase import Client, ColumnDescriptor, Mutation


# make socket 这里配置的是hbase zookeeper的地址，因为master只负责负载均衡，读写由zookeeper协调
transport = TSocket.TSocket('localhost', 9090)
# buffering is critical . raw sockets are very slow
transport = TTransport.TBufferedTransport(transport)
# wrap in a protocol
protocol = TBinaryProtocol.TBinaryProtocol(transport)
# create a client to use the protocol encoder
client = Client(protocol)

# connect
transport.open()

t = 'tab2'


# 扫描所有表获取所有表名称
print 'scanning tables ......'
for table in client.getTableNames():
    print 'found:%s' % table
    if client.isTableEnabled(table):
        print ' disabling table: %s' % t
        # 置为无效
        client.disableTable(table)
        print 'deleting table: %s' % t
        # 删除表
        client.deleteTable(table)


# 创建表
columns = []
col = ColumnDescriptor()
col.name = 'entry:'
col.maxVersions = 10
columns.append(col)
col = ColumnDescriptor()
col.name = 'unused:'
columns.append(col)

try:
    print 'creating table : % s' % t
    client.createTable(t, columns)
except Exception, ae:
    print 'Warn:' + ae.message


# 插入数据
invalid = 'foo-\xfc\xa1\xa1\xa1\xa1\xa1'
valid = 'foo-\xE7\x94\x9F\xE3\x83\x93\xE3\x83\xBC\xE3\x83\xAB'

# non-utf8 is fine for data
mutations = [Mutation(column='entry:foo', value=invalid)]
print str(mutations)
client.mutateRow(t, 'foo', mutations)  # foo is row key

# try empty strings
# cell value empty
mutations = [Mutation(column='entry:foo', value='')]
# rowkey empty
client.mutateRow(t, '', mutations)

#this row name is valid utf8
mutations = [Mutation(column='entry:foo', value=valid)]
client.mutateRow(t, valid, mutations)


# run a scanner on the rows we just created
# 全表扫描
print 'starting scanner...'
scanner = client.scannerOpen(t, '', ['entry:'])

r = client.scannerGet(scanner)
while r:
    #printRow(r[0])
    r = client.scannerGet(scanner)
print 'scanner finished '

# 范围扫描
columnNames = []
for (col, desc) in client.getColumnDescriptors(t).items():
    print 'column with name:', desc.name
    print desc
    columnNames.append(desc.name + ':')

print 'stating scanner...'
scanner = client.scannerOpenWithStop(t, '00020', '00040', columnNames)

r = client.scannerGet(scanner)
while r:
    # printRow(r[0])
    r = client.scannerGet(scanner)

client.scannerClose(scanner)
print 'scanner finished'

# 关闭socket
transport.close()













