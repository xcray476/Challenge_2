infile = open("classnumbers.txt", "r")

content = []

pstring = infile.readline()
while pstring:
    content.append
    pstring = infile.readline

infile.close()

content2 = []

for elem in content:
    elem2 = elem.lower()
    content2.append(elem2)

outfile = open("classnumbers.txt", "w")

for elem3 in content2:
    outfile.write(elem3 + '\n')


outfile.close()