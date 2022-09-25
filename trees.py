# this part of code focuses on trees.

# node class which creates the object and its properties.
class Node:
  def __init__(this,value):
    this.value=value
    this.left=None
    this.right=None



class BinaryTreees:
  def __init__(this):
    this.root=None
   
  def __repr__(self): 
    return  str(self.root.value) 
  #insert method which inserts the class
  def insert(this,value):
    newNode= Node(value)
    if(this.root==None):
      this.root=newNode
      
      
    else :
      pointer=this.root
      while(pointer):
        if(value<pointer.value):
          if(pointer.left): pointer=pointer.left
          else:
            pointer.left=newNode
            return this.root
        elif(value>pointer.value):
          if(pointer.right):pointer=pointer.right
          else:
            pointer.right=newNode
            return this.root

  # this method turns out to have a better approach.
  #
  # def insert_two(this,value):
     
  #      node=Node(value)
  #   if(this.root==None):
  #     this.root=node
  #     return
  #   q=[]
  #   q.append(this.root)
  #   while(len(q)):
  #     temp=q[0]
  #     q.pop(0)
      



      



    
  def lookup(this.value):
    if(this.root==None):return None
    pointer=this.root
    while(pointer):
      if(value>pointer.value):
    