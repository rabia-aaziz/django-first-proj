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

# class house:
#     def rooms():
#         print("There are 4 rooms")
#     def kitchens():
#         print("There are 2 kitchens")
        
        
        
# obj_kitchen = house
# obj_kitchen.kitchens()

# obj_room = house
# obj_room.rooms() 

# -----------------practice-class------------------


# ---------create Id array from 1to 10-------------------------------

# array1 = np.arange(1,11)
# print("array1", array1)

# ---------perform element-wise multiplication 2 arrays by generating arrays------------
# array1 = np.arange(1,11)
# print("array1", array1)

# array2 = np.arange(11,21)
# print("array2", array2)


# multip = array1 * array2
# print("multip",multip)

# ---------------Create 1D array & calculate mean of array--------------------------------------

# mean_array = np.arange(0,10)
# print("Mean of Random Array",np.mean(mean_array))

# ------------Generate 3D array by using Random array------------------------------------------

# randomArray_3d = np.random.rand(4,5,3)
# print("Random Array 3D",randomArray_3d)

# -----------------Generate 3D array by using range-------------------------------------
# range3d = np.arange(11)
# shape = np.reshape(range3d, (5, 2, 1))

# print("range",shape)

# ----------------------Generate 2D array by then apply slicing by(subarrays)

# range3d = np.arange(1,11)
# shape = np.reshape(range3d, (5, 2, 1))
# print(shape)


# range2d = np.arange(1,21)
# shape = np.reshape(range2d, (5, 4))
# print(shape)

# subarray = shape[1:5,1:3]
# print("subarray of 2d array", subarray)

#---------------- linspace 7 equal spaced elements 0-100-----------------

# linSpace = np.linspace(0,100,7)
# print("linSpace",linSpace)


