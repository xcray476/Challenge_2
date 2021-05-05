def color(x,y):
    x1 = str(x)
    y1 = str(y)
    if y1 in x1:
        print("true")
    if y1 not in x1:
        print("false")
    



x1 = "My favorite color: red."
print(x1)


y1 = input("red.")
print(y1)


ans = color(x1, y1)
print("Is my favorite color red? ", ans)

