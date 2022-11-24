#Dictionary comprehension
#from video #50

names = [("name", "Kalob"), ("occupation", "Coder")]
d = {}
for key, value in names:
    d[key] = value
print(d)

d = dict(names)
print(d)

d = {key: value if value != 'Kalob' else 'Mohamed'  for key, value in names}
print(d)

d = {key: value if key != 'name' else 'Mohamed'  for key, value in names}
print(d)

