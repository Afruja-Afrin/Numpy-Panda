import pandas as pd
# print(pd.__version__) # printing version of panda

# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# series = pd.Series(data, index=["apartment #1", "apartment #2", "apartment #3"])


# print(series)

# print(series.loc["a"]) #loc(location)
# print(series.iloc[0]) #integer location(by default)

# series.loc["c"] = 200
# print(series)

# #filtering by value
# print(series[series >= 200])
# print(series[series < 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
series.loc["Day 3"] += 500

print(series.loc["Day 3"])

# filter by values
print(series[series < 2000])




# python panda.py