#get user input
answer = input("Input: ")

#print output
print("Output: ", end="")
print("")

#loop through every letter
for letter in answer:

    #check if it is a vowel or not
    if not letter.lower() in ['a','e','i','o','u']:
        print(letter, end="")



#print new line
print()
