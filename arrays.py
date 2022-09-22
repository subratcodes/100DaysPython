def casting(n):
  n=str(n)
  result=''

  for x in range(0,len(n)):
    if(n[x]=='0'):result+='5'
    else: result+=n[x]
  return result