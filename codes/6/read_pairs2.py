with open('pairs.dat', 'r') as infile:
    text = infile.read()

text = '[' + text.replace(')', '),') + ']'
pairs = eval(text)

import pprint
pprint.pprint(pairs)
