class Person:
    def __init__(self, name, mobile=None, \
                 office=None, email=None):
        self.name, self.mobile= name, mobile
        self.office, self.email = office, email
    def add_mobile(self, number): self.mobile = number
    def add_office(self, number): self.office = number
    def add_email(self, address): self.email = address
    def dump(self):
        s = self.name + '\n'
        for x in ['mobile', 'office', 'email']:
            if eval('self.'+x) is not None:
                s += '%s: %s\n' % (x, eval('self.'+x))
        print(s)

p1 = Person('Zhou', email='zhou@nbu.edu.cn')
p1.add_mobile('18888888888')
p2 = Person('Yang', office='87609384')
p2.add_email('yang@nbu.edu.cn')

phone_book = [p1, p2] # 列表
for p in phone_book:
    p.dump()
    
phone_book = {'Zhou': p1, 'Yang': p2} # 字典
for p in phone_book:
    phone_book[p].dump()
