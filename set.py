#set

my_set = {1,2,3,4,5,1, 2}
print(my_set)
print(len(my_set))

for x  in my_set:
    print(x)

my_set.discard(5)
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7,8])
print(my_set)

#tuples
my_tuple = (1,2,3,4,5,6)
print(my_tuple)
print(my_tuple[2])