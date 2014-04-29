# --*-- coding:utf-8 --*--
import datetime


def getRecords(name):
    pstr = '%Y-%m-%d'
    records = []
    with open('price.txt', 'r') as myf:
        lines = myf.readlines()
        for lin in lines:
            if not lin.startswith(name):
                continue
            arr = lin.split()
            t = datetime.datetime.strptime(arr[6], pstr)
            records.append((t, float(arr[2]), arr[6], arr[2]))
    # 去重
    records = list(set(records))
    # 排序
    records.sort(cmp=lambda x, y: cmp(x[0], y[0]))
    # 平滑处理:价格为0的都去掉
    records = [r for r in records if r[1]]
    return records


if __name__ == '__main__':
    recs = getRecords('土豆')
    for r in recs:
        print r