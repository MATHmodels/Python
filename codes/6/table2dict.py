infile = open('table.dat', 'r')
lines = infile.readlines()
infile.close()
data = {}
properties = lines[0].split()
for p in properties:
    data[p] = {}

for line in lines[1:]:
    words = line.split()
    i = int(words[0])
    values = words[1:]
    for p, v in zip(properties, values):
        if v != 'no':
            data[p][i] = float(v)

import pprint
pprint.pprint(data)
