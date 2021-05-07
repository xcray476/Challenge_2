a = ["Hi!"]*4

b = ["5"]*2

c = ["6"]*8


for elem in a:
   print(elem)

for elem2 in b:
   print(elem2)

for elem3 in b:
   print(elem3)

newlst = []

for elem in a:
    newlst.append(elem)
for elem2 in b:
    newlst.append(elem2)
for elem3 in c:
    newlst.append(elem3)

print(newlst)