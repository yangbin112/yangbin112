import re #导入模块
class Stack(object):
    #初始化栈为列表
    def __init__(self):
        self.stack = []
    #判断栈是否为空
    def isEmpty(self):
        return self.stack==[]
    #返回栈顶元素
    def peek(self):
        return self.stack[-1]
    def peek1(self):
        return self.stack[-2]
    #返回栈的大小
    def size(self):
        return len(self.stack)
    #入栈
    def push(self, item):
        self.stack.append(item)
    #出栈
    def pop(self):
        return self.stack.pop()
	#查看栈内的元素
    def show(self):
        print(self.stack)


st = Stack() #定义栈
t1 = 0 #t1计数switch
t2 = 0 #t2计数case数
t3 = 0 #t3计数if-else的数
t4 = 0 #t4计数if-elseif-else的数
flag = 0
total = 0 #total计数关键词

f = open(r"D:\daima.txt","r",encoding="utf-8") #打开文件
data = f.read() #读文件

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

f.seek(0) #回到文件开头
i = 0
k = len(f.readlines()) #总行数
f.seek(0)
for i in range(k):
    data = f.readline().strip() #一行一行读
    res = re.findall(r'\bswitch\b',data)
    if len(res) >0: #找到switch结构
        flag = 1
        continue #进入下一行
    if flag == 1: #switch结构内
        res = re.findall(r'\bcase\b', data)
        t2 = t2 + len(res)
        res = re.findall(r'\bdefault\b', data)
        if len(res) >0: #遇到default退出
            flag = 0
            print(t2,end=' ')
            t2 = 0 #t2清零
print() #换行

f.seek(0)
k = len(f.readlines())
f.seek(0)
for i in range(k):
    data = f.readline().strip()

    res = re.findall(r'\bif\b', data)
    res1 = re.findall(r'\belse\b', data)
    res2 = re.findall(r'{',data)
    res3 = re.findall(r'}', data)
    #入栈时1代表 if 2代表 else 3代表 {
    if (len(res) > 0) and (len(res1) == 0): #此行只有if没else
        st.push(1) #1入栈
    if (len(res) > 0) and (len(res1) > 0): #既有if又有else
        st.push(2) #2入栈
    if (len(res1) > 0) and (len(res) == 0): #此行只有else没if
       if st.isEmpty() == False and st.peek() == 2  : #栈不为空且栈顶为2,是属于if-elseif-else的
           t4 = t4 + 1
           while st.peek() == 2:#删除队列中所有的elseif
               st.pop()
           st.pop()#删除if
       if st.isEmpty() == False and st.peek() == 1  :#是属于if-else的
           t3 = t3 + 1
           st.pop()#删除if
    if (len(res2) > 0):
               st.push(3)  # 3入栈
    if (len(res3) > 0) :#是}时
        if st.peek() == 3:
            st.pop() #消括号
        elif (st.isEmpty() == False and st.peek() == 2) or (st.isEmpty() == False and st.peek() == 1):
            while st.peek() != 3: #一直删到与其匹配的{
                st.pop()
            st.pop() #删掉该{
print(t3,end=' ')
print(t4)

f.close() #关闭文件