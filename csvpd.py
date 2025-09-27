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


# #to print complete csv file(shows every row)
# print(df.to_string( ))


# #SELECTION BY COLUMN
# print(df["BloodGroup"].to_string())

# #to print more than one column
# print(df[["Name", "BloodGroup", "Hall"]].to_string())


# Drop columns where all values are NaN
df.dropna(axis=1, how='all', inplace=True)

# # indexing bye "Name"
df.set_index('Name', inplace=True)
# print(df)
# #SELECTION BY ROWS
# print(df.loc["Momtaz"])
# # indexing by integer location after indexing by other values
# print(df.iloc[0])


# # printing only the blood group and hall of Subrina
# print(df.loc["Momtaz",["BloodGroup","Hall"]])

# # printing only the blood group and hall of everyone from Afrin to Nasrin
# print(df.loc["Afrin": "Nasrin",["BloodGroup","Hall"]])

# # printing only the blood group and hall of everyone from Afrin to Nasrin by integer location, every location should be integer. every location used in iloc must be integer. be it column or row
# # Here ith:jth, ith is inclusive and jth is exclusive
# print(df.iloc[0:3, [0, 2]])

stud = input("Enter a student name: ")

try:
    print(df.loc[stud])
except KeyError:
    print(f"{stud} not found")

# python csvpd.py


