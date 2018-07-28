tmp=int(raw_input("enter amount of numbers to be stored:"))
list= [0] * tmp
for i in range (tmp):
     tmp2=int(raw_input("enter integer:"))
     list[i]=tmp2
i=0
for i in range (tmp):
     print list[i]
i=0
for i in range (tmp-1):
    j=i
    for j in range (tmp-i-1):
        if(list[j]>list[j+1]):
            tmp2=list[j+1]
            list[j+1]=list[j]
            list[j]=tmp2
i=0
for i in range (tmp):
    print list[i]
