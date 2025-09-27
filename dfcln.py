# Data cleaning = the process of mixing/ removing
# incomplete, incorrect, or irrelevant data.
# ~75% of work done

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

# # 1. Drop irrelevant columns
# df = df.drop(columns=["Hall", "District"])

# 2. Handle missing data
# df = df.dropna(subset=["BloodGroup"]) #value is NaN

# # fill all the NaN values with None
# df = df.fillna({"BloodGroup": "None"})

# # 3. Fix inconsistent values. we can pass more than one key: value pair
# df["BloodGroup"] = df["BloodGroup"].replace({"A+": "AB+"})


# # 4. Standardize text
# df["BloodGroup"] = df["BloodGroup"].str.lower()


# # 5. Fix data types
# df["BloodGroup"] = df["BloodGroup"].astype(bool)


# Remove duplicate values(rows actually)
df = df.drop_duplicates()


print(df.to_string())

