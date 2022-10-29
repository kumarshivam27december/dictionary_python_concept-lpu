# creating an empty set
b=set()
print(type(b))

# adding values to an empty set 
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add(5)


# #accessing elements
# kitne baar bhi add kare vo ek baar hi add hoga becuse set is a collection of non repetative elements
# b.add([4,5,6])# kyoki list/ dictionary ke content ko baad me change kiya ja sakta hai isliye ye isme add nahi hoga syntax error dega
# tuples ko daal sakta 
b.add((4,5,6))
print(b)


# #length of the set
print(b)
print(len(b)) #print the length of the set

# removal of an item
b.remove(5)# removes 5 from the set b
# b.remove(15) # throws an error while trying to remove 15(which is not present in the set)
print(b)
print(b.pop())


