def majorleague_baseball(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "majorleague_baseball"
    if input % 3 == 0:
        return "majorleague"
    if input % 5 == 0:
        return "baseball"
    return input
    

print(majorleague_baseball(15))
    