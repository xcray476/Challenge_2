l1 = ["8", "9", "6", "1", "3", "78"]
    



l2 = ["red", "blue", "yellow", "pink", "teal"]




l3 = ["red", "green", "blue"]

for elem in l1:
    print(elem)

for elem2 in l2:
    print(elem2)

for elem3 in l3:
    print(elem3)    

newlst = []

for elem in l1:
    newlst.append(elem)
for elem2 in l2:
    newlst.append(elem2)
for elem3 in l3:
    newlst.append(elem3)

print(newlst)