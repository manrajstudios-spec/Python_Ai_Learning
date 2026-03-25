import pandas as pd
"""

# nomal 
numbers = ["A","B","C","D",10]

series = pd.Series(numbers)

print(series)

#labels changing 

nums = [1,2,3,4]
series_n = pd.Series(nums , index=['a','b','c','d']) 
print(series_n)



#accesing values using labels
n_nums = [60,70,50,20,100]

n_series = pd.Series(n_nums , index = ["a","b","c","d","e"])

# print(n_series.loc["a"]) #series.loc[label] for accessing using label
# print(n_series.iloc[0])#series.iloc[index] for accessing using index

# #to change Value at a index 
# n_series[0] = 1000 #index 
# n_series.loc[1] = 1000#using label
# n_series.iloc[2] = 2000#using index
# print(n_series)

#filtering
series_filetered = n_series[n_series > 50]
print(series_filetered)
print(n_series[n_series > 20])

"""

#making series using dictionary

scores = {"Maths":100,
         "Physics":90,
         "Chemistry":89,
         "CS":95,
         "English":90
        }

series_d = pd.Series(scores)

print(series_d)
print(series_d.loc["Maths"])
print(series_d.loc["Chemistry"])
print(series_d.loc["Physics"])