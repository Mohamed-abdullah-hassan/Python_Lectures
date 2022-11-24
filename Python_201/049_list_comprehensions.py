#List Comperhension
#From video #49

numers1 = []
for num in [1,3,6,2,9,17]:
    numers1.append(num**2)
print(numers1)


numbers2 = [num**2 for num in [1,3,6,2,9,17]]
print(numbers2)


numbers3 = [num**2 for num in [1,3,6,2,9,17] if num >5 ]
print(numbers3)

names = ['mohamed', 'soliman', 'maged', 'noor', 'kasem']


names1 = [nam.capitalize() for nam in names ]
print(names)
print(names1)

rem = ['noor', 'maged']

names2 = [nam.capitalize() for nam in names if nam not in rem]
print(names)
print(names2)

newlist = [x.capitalize() if x.lower() != "kasem" else "karem".capitalize() for x in names]
print(newlist)