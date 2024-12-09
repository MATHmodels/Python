data = [[ 0.75,  0.29, -0.29, -0.75,  0.29,  0.11, -0.11],
        [-0.29, -0.11,  0.11,  0.29, -0.75, -0.29,  0.29]]

outfile = open('table.txt', 'w')

for row in data:
    for column in row:
        outfile.write('%8.2f' % column)
    outfile.write('\n')
outfile.close()
