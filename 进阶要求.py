import re #导入模块
f = open(r"D:\daima.txt","r",encoding="utf-8")
flag = 0
k = len(f.readlines())
f.seek(0)
t2 = 0
for i in range(k):
    data = f.readline().strip()
    res = re.findall(r'\bswitch\b',data) #找到switch结构
    if len(res) >0:
        flag = 1
        continue
    if flag == 1:
        res = re.findall(r'\bcase\b', data)
        t2 = t2 + len(res)
        res = re.findall(r'\bdefault\b', data) #遇到default退出
        if len(res) >0:
            flag = 0
            print(t2)
            t2 = 0 #t2清零
f.close()
