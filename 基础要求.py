import re #导入模块
f = open(r"D:\daima.txt","r",encoding="utf-8")
data = f.read() #读文件
total = 0 #total计数关键词
t1 = 0 #t1计数switch
res = re.findall(r'\bdo\b',data) #从data里面查do的列表
total += len(res) #用len算do的个数
res = re.findall(r'\bauto\b',data)
total += len(res)
res = re.findall(r'\bbreak\b',data)
total += len(res)
res = re.findall(r'\bcase\b',data)
total += len(res)
res = re.findall(r'\bchar\b',data)
total += len(res)
res = re.findall(r'\bconst\b',data)
total += len(res)
res = re.findall(r'\bcontinue\b',data)
total += len(res)
res = re.findall(r'\bdefault\b',data)
total += len(res)
res = re.findall(r'\bdouble\b',data)
total += len(res)
res = re.findall(r'\belse\b',data)
total += len(res)
res = re.findall(r'\benum\b',data)
total += len(res)
res = re.findall(r'\bextern\b',data)
total += len(res)
res = re.findall(r'\bfloat\b',data)
total += len(res)
res = re.findall(r'\bfor\b',data)
total += len(res)
res = re.findall(r'\bgoto\b',data)
total += len(res)
res = re.findall(r'\bif\b',data)
total += len(res)
res = re.findall(r'\bint\b',data)
total += len(res)
res = re.findall(r'\blong\b',data)
total += len(res)
res = re.findall(r'\bregister\b',data)
total += len(res)
res = re.findall(r'\breturn\b',data)
total += len(res)
res = re.findall(r'\bshort\b',data)
total += len(res)
res = re.findall(r'\bsigned\b',data)
total += len(res)
res = re.findall(r'\bsizeof\b',data)
total += len(res)
res = re.findall(r'\bstatic\b',data)
total += len(res)
res = re.findall(r'\bstruct\b',data)
total += len(res)
res = re.findall(r'\bswitch\b',data)
total += len(res)
t1 = len(res)
res = re.findall(r'\btypedef\b',data)
total += len(res)
res = re.findall(r'\bunion\b',data)
total += len(res)
res = re.findall(r'\bunsigned\b',data)
total += len(res)
res = re.findall(r'\bvoid\b',data)
total += len(res)
res = re.findall(r'\bvolatile\b',data)
total += len(res)
res = re.findall(r'\bwhile\b',data)
total += len(res)
print(total)
print(t1)
f.close()