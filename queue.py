class Queue:

    def __init__(self) -> None:
        self.qu=list()
    
    def enqueue(self,data):
        self.qu.append(data)
    
    def dequeue(self):
        if len(self.qu)==0:
            return ("Underflow")
        else:return self.qu.pop(0)

    def size(self):
        return len(self.qu) 
    
    def isEmpty(self):
        if len(self.qu)==0:
            return True
        else:
            return False

    def front(self):
        if len(self.qu)==0:
            return ("Empty")
        else:
            return self.qu[0]

    def rear(self):
        if len(self.qu)==0:
            return ("Empty")
        else:return self.qu[-1]

    def __str__(self) -> str:
        if len(self.qu)!=0:
            st=""
            for i in range(len(self.qu)):
                st+=str(self.qu[i])+"\t" 
            
            return st
        else:return "Empty"
    
