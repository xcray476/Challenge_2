def color(x,y):
    x2 = str(x)
    y2 = str(y)
    if y2 in x2:
        rstr = "true"
    if y2 not in x2:
        rstr = "false"
    return rstr



x2 = "My favorite color: red."
print(x2)


y2 = input("red.")
print(y2)


ans = color(y2, x2)
print("color, ans")


print("rstr")
