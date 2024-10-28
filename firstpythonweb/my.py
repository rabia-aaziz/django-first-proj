# import random

# number = random.randint(1,10)
# print(number)


# i = 1
# while(i<=10):
#     userInput = int(input("Input your number : "))

#     if (userInput == number):
#         print("you won")
#         break
#     else:
#         i +=1
#         if (i == 2):
#                 print("you have 4 tries")
            
#         elif(i == 3):
#             print("you have 3 tries")
            
#         elif(i == 4):
#             print("you have 2 tries")

#         elif(i == 5):
#             print("you have 1 tries")

#         else:
#             print("you lose")

#     userInputTwo = input("You want to continue : ")
#     if userInputTwo == "Yes":
#             print("continue",i)
#             break
#     else:
#         print("thanks for playing")

# number = 50

# userInput = int(input("Input your Percentage : "))
# if userInput>= 80:
#             print("A+")
# elif userInput >= 70:
#     print("A")
    
# elif userInput >= 60:
#     print("B")
# elif userInput >= 50:
#     print("C")
# else:
#     print("Fail")

class house:
    def rooms():
        print("There are 4 rooms")
    def kitchens():
        print("There are 2 kitchens")
        
        
        
obj_kitchen = house
obj_kitchen.kitchens()

obj_room = house
obj_room.rooms() 

