infile = open('cities_temp.txt', 'r')
temps = {}
for line in infile.readlines():
    city, temp = line.split(':')
    temps[city] = float(temp)
infile.close()
