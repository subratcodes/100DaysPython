class Node:

  def __init__(self,value):
    self.value=value
    self.next=None
  

class LinkedList:
  def __init__(self,value):
    newNode=Node(value)
    self.head=newNode
    self.tail=newNode
    self.length=1



  def insert(self,value):
    newNode=Node(value)
    if(self.head==None):
      self.head=newNode
      self.tail=newNode
      self.length+=1
      return 1
    else:
      self.tail.next=newNode
      self.tail=newNode
      self.length+=1
      return 1

  def printElements(self):
    if(self.head==None): return None
    else:
      temp=self.head
      while(temp):
        print(temp.value,end="")
        temp=temp.next
        
        

# doubly linked list


