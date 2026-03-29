import pandas as pd

#-------------SERIES-----------------------------

#series is just a single column like data in single colomn of spreadsheet (1D)

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

print(n_series.loc["a"]) #series.loc[label] for accessing using label
print(n_series.iloc[0])#series.iloc[index] for accessing using index

# #to change Value at a index 
n_series.loc[1] = 1000 #using label
n_series.iloc[2] = 2000 #using index
print(n_series)

#filtering
series_filetered = n_series[n_series > 50]
print(series_filetered)
print(n_series[n_series > 20])

#making series using dictionary

scores = {"Maths":80,
         "Physics":50,
         "Chemistry":60,
         "CS":95,
         "English":30
        }

series_d = pd.Series(scores)


print(series_d)

#changing values
series_d["Maths"] -= 10

print(series_d["Maths"])
print(series_d["Chemistry"])
print(series_d["Physics"])

#filtering

failed = series_d[series_d < 70]
print(failed)


