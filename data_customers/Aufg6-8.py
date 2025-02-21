import pandas as pd
import os


# df = pd.read_csv("02\data_customers\data\customer_attrition_0.csv", delimiter="|")
csv_files = [f for f in os.listdir("./data_customers/data") if f.endswith('.csv')]
df_list = [pd.read_csv(os.path.join("./data_customers/data", file), delimiter="|") for file in csv_files]
df = pd.concat(df_list, ignore_index=True)
print(df.shape)

print(df["num_kids"].value_counts())

# print(df.info())

print(f"Duplikate: {df.duplicated().sum()}")

def get_amountOf_male_over_50_not_from_france(df):
    return df.loc[
        (df["gender"] == "Male") &
        (df["age"] > 50) &
        (df["country"] != "France")
    ].shape[0]

def get_average_age_by_gender(df, gender):
    return df.loc[
        (df["gender"] == gender)
    ]["age"].mean()

def get_credit_score_from_greatest_balance(df):
    return df.loc[
        df["balance"] == df["balance"].max()
    ]["credit_score"].values[0]

# print(get_amountOf_male_over_50_not_from_france(df))
# print(get_average_age_by_gender(df, "Female"))
# print(get_credit_score_from_greatest_balance(df))
