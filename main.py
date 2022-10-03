import arrays as easyProb
from trees import BinaryTreees
from linkedList import LinkedList
from slidingWindow import SubArray_with_given_sum


# Btree=BinaryTreees()
# Btree.insert(2)
# Btree.insert(3)
# Btree.insert(1)
# a=Btree.lookup(0)
# print(a)

# test=LinkedList(2)
# a=test.insert(3)
# a=test.insert(4)
# print(a)

# test.printElements()
arr=[1,2,3,7,5]
a=SubArray_with_given_sum(arr,len(arr),12)
print(a)