import pandas as pd

data = {
    "Name": ["Afrin", "Miraz", "Murad"],
    "Age": [24, 19, 12]
}

df = pd.DataFrame(data, index=["Siblings 1", "Siblings 2", "Siblings 3"])

# print(df)
# print(df.loc["Siblings 2"])
# print(df.iloc[0])

# Add a new column
# df["Job"] = ["Student", "Employee", "Student"]
# print(df)

# # Add a new row
# new_row = pd.DataFrame([{"Name": "Juthy", "Age": 20, "Job": "Housewife"}],
#                        index=["Siblings 4"])
# df = pd.concat([df, new_row])

# print(df)

# Add new rows
new_rows = pd.DataFrame([{"Name": "Juthy", "Age": 20, "Job": "Housewife"},
                         {"Name": "Mamun", "Age": 17, "Job": "Student"}],
                       index=["Siblings 4", "Siblings 5"])
df = pd.concat([df, new_rows])

print(df)


# python pddf.py
