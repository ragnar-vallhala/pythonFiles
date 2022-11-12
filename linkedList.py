class Node:

    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class linkedList:

    def __init__(self) -> None:
        self.head=None

    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
            
    
    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
        
    def sortedInsert(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            if self.head.data>data:
                self.insert(data)
            else:
                cur=self.head
                while data>cur.data and cur.next!=None:
                    cur=cur.next
                temp=cur.next
                cur.next=Node(data)
                cur.next.next=temp
                
        
    def removeBeginning(self):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head.next
            self.head=temp
    
    def removeEnd(self):
        if self.head==None:
            print("Empty")        
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    
    def delValue(self,data):
        if self.head==None:
            print("Empty")
        else:
            cur=self.head
            if cur.data==data:
                self.removeBeginning()
            else:
                while cur.next.data!=data and cur.next.next!=None:
                    cur=cur.next
                if cur.next.data==data:
                    temp=cur.next.next
                    cur.next=temp
                else:print("Not found")
    
    def display(self):
        st=""
        cur=self.head
        if self.head==None:
            print("Empty")
        else:
            while cur.next!=None:
                st+=str(cur.data)+" -> "
                cur=cur.next
            st+=str(cur.data)
            return st
                
