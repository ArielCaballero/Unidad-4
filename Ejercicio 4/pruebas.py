a="55+1+6/2+7-4*5"
print(a)
b=a.split('+')
print(b)
for i in range(len(b)):
    c=b[i].split("-")
    print(c)
    if b[i]!=None:
        b.pop(i)
        for elemento in c:
            elemento="-"+elemento
            b.insert(i,elemento)
print (b)
for j in range(len(b)):
    c=b[i].split("*")
print (b)