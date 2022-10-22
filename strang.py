def isogram(s):
    if (len(s) == 0): return 0
    map = {}
    for x in range(0, len(s)):
        if (s[x] in map):
            return 0
        else:
            map[s[x]] = 1
    return 1


def print_first_letter(String):
    if (len(String) == 0): return -1
    result = ''

    for x in range(0, len(String)):
        if (x == 0): result += String[x]
        elif (String[x].isspace()):
            result += String[x+1]
    return result


def uncommon_chars(A,B):
  
  result=[]
  for x in A:
    found=False  
    for y in B:
      if (x==y):
        found=True
        break;
    if(found):continue
    else:
      if x not in result:result.append(x)

  for x in B:
    found=False
    for y in A:
      if(x==y):
        found=True
        break;
    if found:continue
    else:
      if x not in result:
        result.append(x)

  result.sort()
  print(result)      





def sum_numbers(string):
  temp='0'
  sum=0
  for x in range(0,len(string)):

    if string[x].isdigit():
      
      temp+=string[x]
    else:
      sum+=int(temp)
      temp='0'
  print(sum)
    
      
      
def last_index(string):
  last_index=-1
  for x in range(0,len(string)):
    if string[x]=='1':last_index=x

  print(last_index)
    
      
      

      
      
      
      
      
        
        
        
        
        
        

        
        
        

    
        
          
        
    
  
  
  
  

