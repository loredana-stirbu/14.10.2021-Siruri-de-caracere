lst=str(input("Scrie un sir"))
l1=""
l2=""
l3=""
print("Sirul initial: ", lst)

for i in lst:
    if ((ord(i)>64) and (ord(i)<90)):
        x=chr(ord(i)+1)
        l1+=x
    else:
        l1+=i      
print("Sirul1:", l1)

l2=l1
for i in lst:
    w=l2.replace(("Z"), ("A"))
print("Sirul2:", w) 

l3=w
for i in lst:
    f=l3.replace(' ','-')
print("Sirul3:", f)
