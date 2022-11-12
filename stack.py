class Stack:
    """Stack works on first in last out principle also called FILO. 
    It include __init__,push,pop,size,isEmpty,__str__"""
    def __init__(self) -> None:
        self.st=list()
    
    def push(self,data):
        self.st.append(data)
    
    def pop(self):
        if len(self.st)==0:
            print("Underflow")
        else:
            return self.st.pop(-1)
    
    def size(self):
        return len(self.st)

    def top(self):
        if len(self.st)==0:
            print("Underflow")
        else:return self.st[-1]
    
    def isEmpty(self):
        if len(self.st)==0:
            return True
        else:return False
    
    def __str__(self) -> str:
        temp=""
        for i in range(-1,-len(self.st),-1):
            temp+=str(self.st[i])+" "
        
        return temp
    
a=Stack()
a.push(5)
a.push(10)
a.push(51)
a.push(584)
a.push(648)
print(str(a))
print(a.isEmpty())
print(a.top())
print(a.pop())
print(a.pop())

print(str(a))


