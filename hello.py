num=input()
newlist=[]
mandarin=["零","一","二","三","四","五","六","七","八","九"]
for i in range(len(num)):
    print(mandarin[eval(num[i])],end="")
#for i in newlist:
 #   print(newlist[newlist.index(i)])