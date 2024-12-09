import urllib.request
url = 'https://www.metoffice.gov.uk/pub/data/weather/uk\
/climate/stationdata/oxforddata.txt'
local_file = 'Oxford.txt'
urllib.request.urlretrieve(url, filename=local_file)
infile = open(local_file, 'r')
data = {}; 
data['place'] = infile.readline().strip()
data['location'] = infile.readline().strip()
for i in range(5): infile.readline()

data['data'] ={}
for line in infile:
    columns = line.split()
    year, month = int(columns[0]), int(columns[1])
    if columns[-1] == 'Provisional': del columns[-1]
    for i in range(2, len(columns)):
        if columns[i] == '---':
            columns[i] = None
        elif columns[i][-1] == '*' or columns[i][-1] == '#':
            columns[i] = float(columns[i][:-1])
        else:
            columns[i] = float(columns[i])
    tmax, tmin, air_frost, rain, sun = columns[2:]
    if not year in data['data']: data['data'][year] = {}
    data['data'][year][month] = {'tmax': tmax, 
          'tmin': tmin, 'air frost': air_frost, 'sun': sun}
infile.close()

print(data['data'][2006][2])
