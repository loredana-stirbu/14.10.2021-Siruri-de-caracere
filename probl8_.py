lst="A B C D E F G H I J K L M N O P Q R S T U V W X Y"
l1=""
l2=""
l3=""

for i in lst:
    x=chr(ord(i)+1)
    l1+=x
    b=l1.replace('!',' ')
    s=b.replace('[','A') #am folosit acest replace deoarece in cazul cind vom avea insusi Z in sir(daca creem un sir nou), acesta va fi inlocuit cu urmtorul caracter(el fiind"]"), pe cind noua near trebui sa se reia ciclul de la prima litera din alfabet"
print("Sirul1:", s)

l2=s
for i in lst:
    w=l2.replace(("Z"), ("A"))
    c=w.replace('!',' ')
    k=c.replace('[','A')
print("Sirul2:", k) 

l3=k
for i in lst:
    f=l3.replace(' ','-')
    b=f.replace('[','A')
print("Sirul3:", b)