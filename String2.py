def Test_If_Substring(a, b):
    a1 = str(a)
    b1 = str(b)
    if a1 in b1:
        rstr = "True"
    if a1 not in b1:
        rstr = "False"
    return rstr

#Here is the main body
#Here we create a string, assigning it to a variable
astr = ("Hello my name is Xavier.")
print(astr)
#Let's take an input
bstr = input("Xavier")
print(bstr)
#And we will call the function
Test_If_Substring(a, b)
print("Here is my name? ", ans)