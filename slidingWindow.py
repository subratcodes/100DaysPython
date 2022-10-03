
#implement with sliding windows problems.
def MaxSumSubArray(arr,n,k):

  
    max_sum=0
    for x in range(0,k):
    
     max_sum+=arr[x]
    for y in range(k,n):
      curr_sum+=arr[y]-arr[y-k]
      max_sum=max(curr_sum,max_sum)
    return max_sum
     
    
  

    

  

  






def SubArray_with_given_sum(arr,n,k):
  
  