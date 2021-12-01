import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

print(s.pow(2,3))  # regresa 2**3 = 8
print(s.add(2,3))  # regresa 5
print(s.mul(5,2))  # regresa 5*2 = 10

data = [
    ('boolean', True),
    ('integer', 1),
    ('float', 2.5),
    ('string', 'some text'),
    ('datetime', datetime.datetime.now()),
    ('array', ['a', 'list']),
    ('array', ('a', 'tuple')),
    ('structure', {'a': 'dictionary'}),
]

for t, v in data:
    as_string, type_name, value = s.show_type(v)
    print('{:<12}: {}'.format(t, as_string))
    print('{:12}  {}'.format('', type_name))
    print('{:12}  {}'.format('', value))

# Imprime una lista de los métodos disponibles
print(s.system.listMethods())