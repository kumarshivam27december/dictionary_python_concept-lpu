'''write a program to create a dictionary of hindi 
words with values as their english translation.
provide user with an option to look it up !'''


mydict = {
    "dusman":"enemy",
    "pankha":"fan",
    "dabba":"box",
    "dosti":"friendship",
    "vastu":"items"
    
    
}

print("options are",mydict.keys())
a=input("enter the hindi word\n")
print("The meaning of your word is:",mydict[a])

'''below line wii not throw an error if the key is not 
present in the dictioary

print("The meaning of your word is:",mydict.get(a))

'''
