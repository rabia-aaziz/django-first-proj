import numpy as np


# kilometer = int(input("kilo meter to meter"))

# miles = (kilometer * 0.6) 

# print ("{%0.3f} kilometer is equal to {%0.3f} miles."%(kilometer,miles))


# miles = int(input("miles to kilo meter"))

# kilometer = (miles / 0.6) 

# print ("{%0.3f} miles is equal to {%0.3f} kilometer."%(miles,kilometer))
# ----------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------



# /////python list/////
python_list  =[1,2,3,4,5]
python_result =[x+2 for x in python_list]

print("after adding 2 in python_list", python_result)

# numpy_list//////
nuympy_array = np.array([1,2,3,4,5])
nuympy_result = numpy_array + 2

print("after adding 2 in array elements", numpy_result)

# /////1D dimensions////
array_1d = np.array([1,2,3,4,5])
print("array 1d", array_1d)

# /////2D dimensions////
array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("array 2d", array_2d)

# /////3D dimensions////
array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("array 3d", array_3d)

array_1d = np.array([1,2,3,4,5])
print("array_1d")
print(array_1d)
print("shape of array", array_1d .shape)
print("datatypes of array", array_1d .dtype)
print("dimension of array", array_1d .ndim)

array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("array_2d")
print(array_2d)
print("shape of array", array_2d .shape)
print("datatypes of array", array_2d .dtype)
print("dimension of array", array_2d .ndim)

array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("array_3d")
print(array_3d)
print("shape of array", array_3d .shape)
print("datatypes of array", array_3d .dtype)
print("dimension of array", array_3d .ndim)



# ------------------------------------------------------------
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# array_result = array1 + array2
# print("array1",array1)
# print("array2",array2)
# print("result",array_result)

# ---------ARITHMATIC OPERTATIONS (numpy)
# --------MULTI DIMENSIONS (2D,3D)
array2d_1 = np.array ([[1,2,3],[4,5,6]])
array2d_2 = np.array ([[7,8,9],[10,11,12]])
add_2d = array2d_1 + array_2d
multi_2d = array2d_1 * array_2d
sub_2d = array2d_1 - array_2d

print("Addition", add_2d)
print("Multiplication", multi_2d)
print("Subtraction", sub_2d)



array3d_1 = np.array([[[1,2,],[3,4]],[[5,6],[7,8]]])
array3d_2 = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])

array_result = array3d_1 + array3d_2
multi_array = array3d_1 * array3d_2
sub_array = array3d_1 - array3d_2
print(" add the array of",array_result)
print("multiply the array of",multi_array)
print("subtract the array of ",sub_array)




array_1 = np.array(["kinza","rabii"])
print("array1",array_1)




array_2 = np.array([["milk","sugar","tea"]])
print("array2",array_2)


array_3 = np.array([[["rice","onion"],["oil","chicken"]],[["garlic","spices"],["tomato","potato"]]])
print("kinrabi biryani Recipe")
print(array_3)


# ////Statistical Operatores/////

array_1d = np.array([10,20,30,40,50])

print("array1d", array_1d)
print("mean:",np.mean(array_1d))
print("sum:",np.sum(array_1d))
print("min:",np.min(array_1d))
print("max:",np.max(array_1d))

array_2d = np.array([[10,20,30],[40,50,60]])

print("array2d", array_2d)
print("mean:",np.mean(array_2d))
print("sum:",np.sum(array_2d))
print("min:",np.min(array_2d))
print("max:",np.max(array_2d))


array_3d = np.array([[[10,20],[30,40]],[[40,50],[60,70]]])

print("array3d", array_3d)
print("mean:",np.mean(array_3d))
print("sum:",np.sum(array_3d))
print("min:",np.min(array_3d))
print("max:",np.max(array_3d))




array1d = np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
print ("array1d", array1d)

array2d = array1d.reshape(3,4)
print("array2d",array2d)