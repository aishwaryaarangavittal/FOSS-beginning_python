list= [""] * 12
for i in range (12):
    str1=raw_input("enter name:")
    list[i]=str1
i=0
for i in range (10):
    strr=list[i]+list[1+i]+list[i+2]
    l=len(strr)-1
    str2=""
    while (l>=0):
       str2+=strr[l]
       l=l-1
    if(strr==str2):
       print "palindrome"
    else:
       print "not palindrome"
