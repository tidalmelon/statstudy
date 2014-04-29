# --*-- coding:utf-8 --*--
import time
import datetime


def utc2local(str_utctime):
    """
    Wed, 02 Apr 2014 03:42:11 GMT => 2014-04-02 11:42:11
    主要用与hadoop日志时间格式解析
    根据需求可用第三方包dateutil实现时区转换
    :param str_utctime:
    :return: 北京时间-> datetime
    """
    local_time = datetime.datetime.strptime(str_utctime, '%a, %d %b %Y %H:%M:%S GMT') + datetime.timedelta(hours=8)
    return local_time


def getCurTimeStamp():
    """
    获取当前时间戳：离1970年1月1日午夜开始的毫秒数
    :return:
    """
    return int(time.time() * 1000)


def str2date(str_date):
    """
    2013-12-08 字符串格式化为日期
    :param str_date:
    :return:
    """
    return time.strptime(str_date, '%Y-%m-%d')


def getDateTicks(list_time):
    """
    输入日期列表返回xLabels
    [t1, t2] => [(2013, 12, 08), (2013, 12, 08)]
    :param list_time:
    :return:
    """
    return [(t.tm_year, t.tm_mon, t.tm_mday) for t in list_time]


def getDateTick(str_date):
    """
    2013-12-08 => (2013, 12, 08)
    :param str_date:
    :return:
    """
    t = time.strptime(str_date, '%Y-%m-%d')
    return t.tm_year, t.tm_mon, t.tm_mday


if __name__ == '__main__':
    print getDateTick('2013-12-08')