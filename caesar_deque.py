from collections import deque
import string
#functions
def mergeletters(newlist):
    newword = ""
    for x in newlist:
        newword = newword + x
    return newword
#main
letters = deque([letter for letter in string.ascii_lowercase])

indexes = []
shiftword = []

userinput0 = input("enter word: ")
userinput = userinput0.strip()
userinput1 = int(input("enter shift (int): "))

for letter in userinput:
    if letter in letters:
        index = letters.index(letter)
        indexes.append(index)
    
letters.rotate(-userinput1) 

for x in indexes:
    shiftword.append(letters[x])
print(mergeletters(shiftword))