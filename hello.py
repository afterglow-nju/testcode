tem=input()

ans=list([])
for i in range(1,len(tem)):
    ans.append(tem[i])
temm="".join(ans)
#print("F{:.2f}".format(eval(temm)))
if tem[0]=="C":
    #del ans[0]
    print("F{:.2f}".format(eval(temm)*1.8+32))
else:
    #del ans[0]
    print("C{:.2f}".format(eval(temm)/1.8-32/1.8))