#!/usr/bin/python

import re
fo= open("dumy.txt","r") 

while True:
  line=fo.readline()
  i="10"
  j="20"
  for k in range(0,18,1):
    if(re.search(i,line)):
       print line
    i=int(i)+int(j)
    i=str(i)
  if not line:
       break
fo.close()





