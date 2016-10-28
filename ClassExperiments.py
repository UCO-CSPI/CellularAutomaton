class cell:
    classattibute = 1

    def __init__(self):
        self.instanceattribute=3

a=cell()
b=cell()
print('a',a.instanceattribute, a.classattibute)
a.instanceattribute = 100
print('a', a.instanceattribute, a.classattibute)
print('b', b.instanceattribute, b.classattibute)
a.classattibute = 200
print('a', a.instanceattribute, a.classattibute)
print('b', b.instanceattribute, b.classattibute)

print('*********** List Example **************')
class Dog:

    kind = 'canine'         # class variable shared by all instances
    tricks = []

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

#initialize instances
d = Dog('Fido')
e = Dog('Buddy')
print('After initialize instances:     {!s:<8}{!s:<10}{!s:<}'.format(d.name, d.kind, d.tricks))
print('After initialize instances:     {!s:<8}{!s:<10}{!s:<}\n'.format(e.name, e.kind, e.tricks))


#append roll over to Fido
d.tricks.append('roll over')
print('After append roll over to Fido: {!s:<8}{!s:<10}{!s:<}'.format(d.name, d.kind, d.tricks))
print('After append roll over to Fido: {!s:<8}{!s:<10}{!s:<}\n'.format(e.name, e.kind, e.tricks))

#set Fido kind to cat
d.kind = 'cat'
print('After set Fido kind to cat:     {!s:<8}{!s:<10}{!s:<}'.format(d.name, d.kind, d.tricks))
print('After set Fido kind to cat:     {!s:<8}{!s:<10}{!s:<}\n'.format(e.name, e.kind, e.tricks))
print(Dog.kind)

#set Fido tricks to list
d.tricks = ['play dead', 'roll over']
print('After set Fido tricks to list:  {!s:<8}{!s:<10}{!s:<}'.format(d.name, d.kind, d.tricks))
print('After set Fido tricks to list:  {!s:<8}{!s:<10}{!s:<}\n'.format(e.name, e.kind, e.tricks))

#append fetch to Fido
d.tricks.append('fetch')
print('After append fetch to Fido:     {!s:<8}{!s:<10}{!s:<}'.format(d.name, d.kind, d.tricks))
print('After append fetch to Fido:     {!s:<8}{!s:<10}{!s:<}\n'.format(e.name, e.kind, e.tricks))

e.asd ='test'
print(e.asd)
print(d.asd)



