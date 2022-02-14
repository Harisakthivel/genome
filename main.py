import random

mylist = ['A','T','G','C','N']
newlist=(random.choices(mylist,  k = 2048))
with open('file.txt', 'w') as f:
    f.writelines(newlist)
    file = open("file.txt", "rt")
data = file.read()

#count
A=(data.count('A'))
T=(data.count('T'))
G=(data.count('G'))
C=(data.count('C'))
AT=(data.count('AT'))
GC=(data.count('GC'))

#percentage_calculation
ap = (A / 2048)*100
tp = (T / 2048)*100
gp = (G / 2048)*100
cp = (C / 2048)*100
atp = (AT / 2048)*100
gcp = (GC / 2048)*100

print('A', A ,ap)
print('T', T ,tp)
print('G', G ,gp)
print('C', C ,cp)
print('AT', AT ,atp)
print('GC', GC ,gcp)
