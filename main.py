import arrays as easyProb

def num_runner():
  sum=1
  
  for x in range(10):
    if(x!=0):
      sum=sum*x



  
  return sum%3







def count(arr,n,x):
  
  if(n==0):return -1
  count=0
  middle_index=int(n/2)

  #there is a possibility that left can be on the other side as well. but surely it is on the right side.
  if(arr[middle_index]==x):
    count+=1
    count+=loop_runner(0,middle_index,x,arr)
    count+=loop_runner(middle_index+1,n,x,arr)
  elif(arr[middle_index]>x):
    count+=loop_runner(0,middle_index,x,arr)
  elif(arr[middle_index]<x): count+=loop_runner(middle_index+1,n,x,arr)
  else: return -1
  if count>0:
    return count
  else :
    return -1


  

#loops can have start and end value on the basis range and parameeters passed.,
def loop_runner(start,end,element,arr):
  temp_count=0
  
  for x in range(start,end):
   
    if(arr[x]==element):temp_count+=1
 
  return temp_count
  

# numbers=[1,1,2,2,2,3,3,3,4,5,6,7]
# a=count(numbers,len(numbers),0)
# print(a)

a=easyProb.casting(100023);
print(a)