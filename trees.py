# node class which creates the object and its properties.
class Node:

    def __init__(this, value):
        this.value = value
        this.left = None
        this.right = None


class BinaryTreees:

    def __init__(this):
        this.root = None

    def __repr__(self):
        return str(self.root.value)

    #insert method which inserts the class
    def insert(this, value):
        newNode = Node(value)
        if (this.root == None):
            this.root = newNode

        else:
            pointer = this.root
            while (pointer):
                if (value < pointer.value):
                    if (pointer.left): pointer = pointer.left
                    else:
                        pointer.left = newNode
                        return this.root
                elif (value > pointer.value):
                    if (pointer.right): pointer = pointer.right
                    else:
                        pointer.right = newNode
                        return this.root


# returns the value by searching using a binary search

    def lookup(this, value):
        if (this.root == None): return None
        pointer = this.root
        while (pointer != None):
            if (value > pointer.value): pointer = pointer.right
            elif (value < pointer.value): pointer = pointer.left
            else: return pointer.value
        return None

    # deletes the array
    def delete(this, value):
        if (this.root == None): return None

        parentNode = this.root
        currentNode = None
        while (currentNode != None):
            if (value < currentNode.value):
                parentNode = parentNode
                currentNode = parentNode.left
            elif (value > currentNode.value):
                parentNode = parentNode
                currentNode = parentNode.right

                # value has been matched

    def traversal(this, root, type):
        if type == 'inOrder':
            if (root is None): return
            this.traversal(root.left, 'inOrder')
            print(root)
            this.traversal(root.right, 'inOrder')
        elif type == 'preOrder':
            if (root is None): return
            print(root.value)
            this.traversal(root.left, 'preOrder')
            this.traversal(root.right, 'preOrder')
        elif type == 'postOrder':
            if root is None: return
            print(this.root)

    def PreorderUsingStack(this):
      if(this.root is None): return None
      result=[]
      stack=[]
      stack.append(this.root)
      while len(stack)!=0:
        temp=stack[-1]
        stack.pop()
        result.append(temp.data)
        if(temp.right): stack.append(temp.right)
        if(temp.left):stack.apppend(temp.left)
      return result
        
    