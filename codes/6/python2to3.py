with open('python2.py', 'r') as pyfile:
    codes2 = pyfile.read().strip()

lines = []
for line in codes2.split('\n'):
    k = line.find('#')
    if k>=0:
        line = line[:k].strip()
    
    k = line.find('.keys()')
    if k>=0:
        line = line.replace('=', '= list(').\
                    replace('.keys()', '.keys() )')

    k = line.find('print ')
    if k>=0:
        line = 'print(' + line.split('print ')[1]+ ')'

    lines.append(line)

codes3 = '\n'.join(lines)

print('\n' + '-'*5 + '转换前的代码' + '-'*5)
print(codes2)
print('\n' + '-'*5 + '转换后的代码' + '-'*5)
print(codes3)
print('\n' + '-'*5 + '代码运行结果' + '-'*5)
exec(codes3)
