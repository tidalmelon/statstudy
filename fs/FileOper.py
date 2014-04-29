__author__ = 'root'
import os
import shutil

dir = '/home/hadoop/Sep-2013'
logs = []
for root, dirs, files in os.walk(dir):
    print dirs
    for name in files:
        s = os.path.join(root, name)
        t = s.replace('/dongxicheng', '-dongxicheng')
        logs.append((s, t))

print logs

for t in logs:
    shutil.move(t[0], t[1])


for relative in os.listdir(dir):
    file = os.path.join(dir, relative)
    if os.path.isdir(file):
        print file
        os.rmdir(file)