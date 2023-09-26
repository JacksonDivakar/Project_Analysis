class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL():
    def __init__(self):
        self.tail=None
    def enqueue(self,data):
        new=Node(data)
        if self.tail is None:
            new.next=new
        else:
            new.next=self.tail.next
            self.tail.next=new
            
        self.tail=new
        
    def __len__(self):
        count=0
        
        itr=self.tail
        if itr:
            while True:
                itr=itr.next
                count+=1
                if itr==self.tail:
                    break
        return count
    def dequeue(self):
        if self.tail is None:
            return "CLL is Empty"
        if len(self)==1:
            val=self.tail
            self.tail=None
        else:
            val=self.tail.next
            self.tail.next=self.tail.next.next
        return val.data
    def display(self):
        itr=self.tail.next
        st=""
        while True:
            
            st+=str(itr.data)+"-->"
            itr=itr.next
            if itr==self.tail:
                break
            
        
L=CLL()
L.enqueue(1)
L.enqueue(2)
L.display()
print(L.dequeue())
print(L.dequeue())
len(L)

        
        
            
        
