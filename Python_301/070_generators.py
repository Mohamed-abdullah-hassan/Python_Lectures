

print('Starting function with 100000000 iteration')
for num in range(10_000_000):
    num = num + num
print('Completed,')


def my_generator():
    for num in range(100_000_000):
        yield num + num

print('\nStarting genrator with 100000000 iteration to note the defrence')
total = my_generator()
print('Completed,')

print(total)
print(type(total))

print("Printing total some list")

# for nn in total:
#     print(nn)
#     if nn > 4_000:
#         break

def my_generator2():
    for num in range(50):
        yield num * num

my_var_gen = my_generator2()

num =0
for multi in my_var_gen:
    print('for ',num,'square is: ',multi)
    num  +=1
    if multi > (20*20):
        print("Stopping")
        break

num_List = list(my_var_gen) #Here my_var_gen exhausted upto 21 * 21 then the list will start from 22 * 22 

print(num_List)
