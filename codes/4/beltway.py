days, lats, longs = [],[],[]

with open('beltway.txt', 'r') as infile:
    infile.readline()
    for line in infile:
        dat = line.split(',')
        
        days.append(int(dat[0].split('/')[1]))
        lats.append(float(dat[1]))
        longs.append(float(dat[2]))

with open('xy.txt', 'w') as outfile:
    outfile.write('%8s %8s\n' % ('long', 'lat'))
    for long, lat in zip(longs, lats):
        outfile.write('%8.4f %8.4f\n' % (long, lat))
