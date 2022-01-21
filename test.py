alp1="abcdefghijklmnopqrstuvwxyz"
alp2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tem=input()
for i in range(len(tem)):
    index1=alp1.find(tem[i])
    index2=alp2.find(tem[i])
    if index1!=-1:
        print(alp1[(index1+3)%26],end="")
    elif index2!=-1:
         print(alp2[(index2+3)%26],end="")
    else: print(tem[i],end="")