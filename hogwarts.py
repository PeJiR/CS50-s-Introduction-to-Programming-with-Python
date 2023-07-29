# students = ["Hermione", "Harry","Ron"]

# print(students[0:3])
##
# students = ["Hermione", "Harry","Ron"]

# for students in students:
#     print (students)

###

# students = ["Hermione", "Harry","Ron"]

# for i in range(len(students)):
#     print(i+1,students[i])
    
###

# students = {"Hermione":"Gryffindor", 
#             "Harry":"Gryffindor",
#             "Ron":"Gryffindor",
#             "Draco":"Slytherin",
# }
 
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
    
 #######
 
 
# students = {
#     "Hermione":"Gryffindor", 
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Slytherin",
# }
# for student in students:
#     print(student,students[student],sep=",")

###
students = [
    {"name":"Hermione", "house":"Gryffindor","patronus":"otter"}, 
    {"name":"Harry", "house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]
for student in students:
    print(student["name"],student ["house"], student["patronus"],sep =",")
    