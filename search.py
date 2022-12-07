class BinarySearch:
  def __init__(self,arr=[]):
    self.array=arr

  def recursion(self,low,high,target):
    if(low>high):return  False
    else:
      mid=int((low+high)/2)
      if target==self.array[mid]: 
        print('Index found at',mid)
        return mid
      elif(target>self.array[mid]):self.recursion(mid+1,len(self.array)-1,target)
      else: self.recursion(0,mid-1,target)

      
        
    
    
  
    


  def iterative(self,target):
    
    low,high=0,len(self.array)-1
    mid=None
    
    
    while low<=high:
      mid=int((low+high)/2)
      if(self.array[mid]==target): return mid
      elif self.array[mid]<target:low=mid+1
      else: high=mid-1

    print(high)
    return high+1

    
      
      
    
    