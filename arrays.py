def casting(n):
  n=str(n)
  result=''

  for x in range(0,len(n)):
    if(n[x]=='0'):result+='5'
    else: result+=n[x]
  return result



def isRotatedEqual(str1,str2):
  
    dictionary = {}
    count=0
    for x in str2:
        dictionary[x]=-1
    for x in str1:
      if x in dictionary:
        if(dictionary[x]==-1):dictionary.update({x:1})
        else :count+=1
      else: count+=1

    print(count)




def firstElementKTime(arr,n,k):

# need to initialise the dictionary first.
  dictionary={}
  for x in range(0,n):
    if(arr[x] in dictionary):
      value=dictionary.get(arr[x])
      if(value+1==k): return arr[x]
      else:dictionary.update({arr[x]:value+1})
    else: dictionary[arr[x]]=1
  return -1


def immediateSmaller(arr,n):

  stack=[arr[0]]
  

  for x in range(1,n):

    if(stack[len(stack)-1]>arr[x]):
      
      arr[x-1]=arr[x]
    else: arr[x-1]=-1
    stack.append(arr[x])

  arr[n-1]=-1
  return arr


  



  


def sort012(arr,n):

  i=0
  j=1
  while(i<j and j<n):
    if arr[i]<arr[j]:
      i+=1
      j+=1
    elif(arr[i]>arr[j]):
      temp=arr[j]
      arr[j]=arr[i]
      arr[i]=temp
      
      

    
    
def min_distance(arr,n,num1,num2):
  min_dist=0
  x_index=-1
  y_index=-1



def binary_recursie(arr,x):

  middle_index=len(arr)-1
  middle_index=middle_index/2



      
    
    

        




#subaary problems


def waveOrder(n,arr):
  i=0 
  j=1
  last_element=n-1
  if(n%2==0):last_element=n-2 

  while(j<=last_element):
    if(j%2!=0):
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j+=1
    else: 
      i+=1
      j+=1
  return arr
    
  
  