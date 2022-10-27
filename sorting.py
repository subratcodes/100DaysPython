


def selectionSort(arr):

  for x in range(0,len(arr)):
    min_index=x
    for y in range(x+1,len(arr)):
      if (arr[y]<arr[min_index]): min_index=y
  
    temp=arr[min_index]
    arr[min_index]=arr[x]
    arr[x]=temp
  return arr


def insertionSort(arr):
  
  

    
        
      
      