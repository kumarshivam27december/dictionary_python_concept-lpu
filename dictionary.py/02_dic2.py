mydict={
    "fast": "in a quick manner",
    "harry":"A coder",
    "shivam":"a student",
    "marks":"[1,2,3,4,5,6,7,8,9,0]",
    "anotherdict": {'shivam':'player'},
    1:2
}


print(list(mydict.keys())) # prints the keys of the dictionary
print(mydict.values()) # prints the values of the dictionary
print(mydict.items()) # prints the items i.e (key,value) for all contents of the dictionary
print(mydict)
updatedict={
    "pankaj":"Friend",
    "shubham":"Friend",
    "satyam":"my brother",
    "sundram":"my brother"
}
mydict.update(updatedict) #update the dictionary by adding key value pairs from updatedict
print(mydict)
print(mydict.get("satyam2")) # prints value associated with key "satyam"
print(mydict["satyam2"]) # print value associated with key "satyam"

# the difference between .get and [] syntax in dictionaries:
print(mydict.get("satyam2")) # returns none as satyam2 is not present in the dictionary
print(mydict["satyam2"]) # throws an error as satyam2 is not present in the dictionary
