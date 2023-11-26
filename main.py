import pandas as pd


# Making a list of missing values types
missing_values = ["n/a", "na", "--", "?"]
df = pd.read_csv("mushroom/agaricus-lepiota-data.csv",
                 na_values=missing_values)

print(df.head())
print(df.describe())

# What are the features?
col_names = ["poisonous", "cap-shape", "cap-surface", "cap-color", "bruises",
             "odor", "gill-attachment", "gill-spacing", "gill-size",
             "gill-color", "stalk-shape", "stalk-root",
             "stalk-surface-above-ring", "stalk-surface-below-ring",
             "stalk-color-above-ring", "stalk-color-below-ring", "veil-type",
             "veil-color", "ring-number", "ring-type", "spore-print-color",
             "population", "habitat"]

# What are the expected types (int, float, string, boolean)?
# string and bools

# Is there obvious missing data(values that Pandas can detect)?
for i in range(len(col_names)):
    print(df[col_names[i]])
    print(df[col_names[i]].isnull())

# Is there other types of missing data that’s not so obvious
# (can’t easily detect with Pandas)?
print("Missing values distribution: ")
print(df.isnull().mean())

print("Total missing values for each feature")
print(df.isnull().sum())

# Check datatype in each column
print("Column datatypes: ")
print(df.dtypes)
