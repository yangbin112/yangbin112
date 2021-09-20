import re
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
st = Stack()
f = open(r"D:\daima.txt","r",encoding="utf-8")
flag1 = 0
t3 = 0
t4 = 0
k = len(f.readlines())
f.seek(0)
for i in range(k):
    data = f.readline().strip()

    res = re.findall(r'\bif\b', data)
    res1 = re.findall(r'\belse\b', data)
    res2 = re.findall(r'{',data)
    res3 = re.findall(r'}', data)
    if (len(res) > 0) and (len(res1) == 0): #此行只有if没else
        st.push(1) #1入栈
    if (len(res) > 0) and (len(res1) > 0): #既有if又有else
        st.push(2) #2入栈


    if (len(res1) > 0) and (len(res) == 0): #此行只有else没if
       if st.isEmpty() == False and st.peek() == 2  : #栈不为空且栈顶为1,是属于if-elseif-else的
           t3 = t3 + 1
           while st.peek() == 2:#删除队列中所有的elseif
               st.pop()
           st.pop()#删除if
       if st.isEmpty() == False and st.peek() == 1  :#是属于if-else的
           t4 = t4 + 1
           st.pop()#删除if
    if (len(res2) > 0):
               st.push(3)  # 3入栈
    if (len(res3) > 0) :#是}时
        if st.peek() == 3:
            st.pop() #消括号
        elif (st.isEmpty() == False and st.peek() == 2) or (st.isEmpty() == False and st.peek() == 1):
            while st.peek() != 3:
                st.pop()
            st.pop()
print(t4)
print(t3)

f.close()