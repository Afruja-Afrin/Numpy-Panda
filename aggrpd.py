# Aggregate Functions = Reduces a set of values into a single summary value 
# Used to summarize and analyze data.
# Often used with the groupby() function

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# to print csv file
# print(df)

df["Name"] = df["Name"].str.split().str[0]
df["Hall"] = df["Hall"].str.split().str[0]
df["Hall"] = df["Hall"].replace("Begum", "Sufia")
df["Hall"] = df["Hall"].replace("A", "KamalUddin")
df["Hall"] = df["Hall"].replace("A.F.M.", "KamalUddin")
df["Hall"] = df["Hall"].replace("Bongobondhu", "Bangabondhu")
df["Hall"] = df["Hall"].replace("Sheikh", "Hasina")
df["Hall"] = df["Hall"].replace("Bangomata", "Bangamata")
df["Hall"] = df["Hall"].replace("Sufiya", "Sufia")
df["Hall"] = df["Hall"].replace("PRITILOTA", "Pritilata")
df["Hall"] = df["Hall"].replace("Pritilota", "Pritilata")


def clean_blood_group(bg):
    bg = str(bg).upper()
    bg = bg.replace(" ", "")
    bg = bg.replace("(VE)", "+").replace("+VE", "+").replace("(+VE)", "+")
    bg = bg.replace("POSITIVE", "+")
    bg = bg.replace("(+)", "+")
    bg = bg.replace("(-VE)", "-").replace("-VE", "-")
    bg = bg.replace("NEGATIVE", "-")
    
    # Only keep valid blood groups
    valid_bgs = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    for v in valid_bgs:
        if v in bg:
            return v
    return bg 
    
# Apply to the BloodGroup column
df["BloodGroup"] = df["BloodGroup"].apply(clean_blood_group)
df["District"] = df["District"].str.title()

df.dropna(axis=1, how='all', inplace=True)
df.set_index('Name', inplace=True)

# ##WORKING ON WHOLE DATAFRAME of aggregate functions
# # find numeric
# print(f"mean = ",df.mean(numeric_only=True)) #mean
# print(f"summation = ",df.sum(numeric_only=True)) #summation
# print(f"minimum = ",df.min(numeric_only=True)) #minimum
# print(f"maximum = ",df.max(numeric_only=True)) #maximum
# print(f"standard deviation = ", df.std(numeric_only=True)) #standard deviation
# print(f"variance = {df.var(numeric_only=True)}") #variance
# #count number of rows of each column
# print(df.count())



# ##WORKING ON SINGLE COLUMN
# print(f"mean = ",df["ID"].mean()) #mean
# print(f"summation = ",df["ID"].sum()) #summation
# print(f"minimum = ",df["ID"].min()) #minimum
# print(f"maximum = ",df["ID"].max()) #maximum
# print(f"standard deviation = ", df["ID"].std()) #standard deviation
# print(f"variance = {df["ID"].var()}") #variance
# print(df["ID"].count())


group = df.groupby("BloodGroup")
print(group["ID"].mean()) #printing average ID of each group
print(group["ID"].min())



# python aggrpd.py
