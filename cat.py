# i = 0
# while i < 3:
#     print("meaow")
#     i += 1

###
    
# for i in [0,1,2]:
#     print("meow")

###

# for i in range (5):
#     print("meow")

###

# for _ in range (5):
#     print("meow")

###

# print("meow\n" * 3)

###

# print("meow\n" * 3, end="")

###

# while True 
#     n=int(input("What's n?"))
#     if n<0:
#         continue 
#     else:
#         

###

# while True:
#     n=int(input("What's n?"))
#     if n>0:
#         break
    
# for _ in range (n):
#     print("meaow")

###

# def main():
#     meaow(3)
    
# def meaow (n):
#     print ("meaow")

# main()

###

def main():
    number = get_number()
    meaow(number)

def get_number():
    while True:
        n = int(input("What's n? ")) 
        if n > 0:
            return n

def meaow(n):
    for _ in range(n):
        print("meaow")

main()



    