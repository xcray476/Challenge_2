x = ["1","2","3"]

y = ["3","4","5"]


print("x is subset of y?", x.issubset(y))
print("x is subset of x?", y.issubset(x))

cstr = input(" please enter character: ")

if y in x:
    print("Yes.")
 
if y not in x:
    print("No.")




