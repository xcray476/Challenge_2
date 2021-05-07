alst = [1, 5, 7, 0]
blst = [8, 4, 3, 9]


newlst = []

for elem in alst:
    print(elem)

for elem2 in blst:
    print(elem2)

for elem in alst:
    newlst.append(elem)
for elem2 in blst:
    newlst.append(elem2)

print(newlst)