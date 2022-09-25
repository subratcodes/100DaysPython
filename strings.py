def isogram(s):
  if(len(s)==0): return 0
  map={}
  for x in range(0,len(s)):
    if(s[x] in map):
      return 0
    else: map[s[x]]=1
  return 1



  def removeConsecutiveCharacter(self, S):
    if(len(s)==0) return False
    length=len(s)
    i=y=0
    result=''
    while(i<length-1):
      