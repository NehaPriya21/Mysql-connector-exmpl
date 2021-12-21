#!/usr/bin/python

import re
fo=open("dumy.txt","r")
while i:
  line=fo.readline()
  if(re.search("ATGATCGATCGATCGATCGT",line)):
    print("found")
  if not line:
    break
fo.close()

