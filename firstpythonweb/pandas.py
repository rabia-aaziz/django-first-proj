import pandas as pd
# ------------------SERIES -hold any type of data---------------------
# a = [1, 2, 3, 4, 5]
# var = pd.Series(a, index = ["x","y","z","a","b"])
# print(var)
# print(var["y"])


# cars = {
#     "BMW": 2,
#     "FERRARI": 3,
#     "HONDA": 1,
#     "AUDI": 4,
#     "CADILLAC": 5,
# }
# myVar = pd.Series(cars, index = ["BMW","HONDA"])

# print(myVar)

# ------------DATAFRAME---------------------

# Define the data dictionary
# data = {
#     'calories': [310, 410, 500],
#     'days': ["monday", "tuesday", "wednesday"],
#     'passing': [2, 6, 7]
# }
# myVar = pd.DataFrame(data,index=["day1","day2","day3"])
# print(myVar)
# print(myVar.loc["day1"])

 df = pd.read_csv('data.csv')
 # print(df)
 print(df.to_string)

        
