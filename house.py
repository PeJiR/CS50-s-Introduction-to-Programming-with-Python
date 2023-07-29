# name = input ("What's your name?")
# if name == "Harry":
#     print ("Gryffindor")
# elif name =="Hermione":
#     print ("Gryffindor")
# elif name == "Ron":
#     print ("Gryffindor")
# elif name == "Draco":
#     print ("Slytherin")
# else:
#     print ("Who?")

###########

# name = input ("What's your name?")
# if name == "Harry" or name =="Hermione" or name == "Ron":
#     print ("Gryffindor")
# elif name == "Draco":
#     print ("Slytherin")
# else:
#     print ("Who?")

###################

# name = input ("What's your name?")
# match name:
#     case "Harry":
#         print ("Gryffindor")
#     case "Hemione":
#         print ("Griffindor")
#     case "Ron":
#         print ("Griffindor")
#     case "Draco":
#         print ("Slytherin")
#     case __:
#         print ("Who?")

################

name = input ("What's your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case __:
        print ("Who are you?")
