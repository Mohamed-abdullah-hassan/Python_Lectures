# Indexing and slicing Iterables From Video #017
# Iterables are object that can be looped or iterated using loops
# Iterables objects is like Arrays, Lists, Sets, Tuples, Dictionary, and Strings
# Indexing is the 'Offcit' of each element in Iterables
# Indexing starts count from 0 --> Head of Iterables

zooLst = ['Cats', 'Dogs', 'Elephant', 'Snakes', 'Birds', 'Animals', 3309,]
myName = "Mohamed Abdullah Hassan"

#To print the First elemnt in zooList which is in index 0
print(zooLst[0])
#To print Snakes which is at Index = 3 
print(zooLst[3])

#To Print range of items by using start_index : stop_index
#nooting that stop_index will not be printed

print(myName[0:7]) 
print(myName[8:16])
print(zooLst[2:6])

#To print from a strt_index to the end of the iterable by using start_index::
print(myName[8::])
#To index elements in backward order by using -start_index which indicates the counting is backward
#nooting that backward counting starts from -1 
print(zooLst[-1])

print(myName[-6::])

print(myName[-15:-7])