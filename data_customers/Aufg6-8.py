import pandas as pd


df = pd.read_csv("02\data_customers\data\customer_attrition_0.csv", delimiter="|")
print(df.shape)

print(df.info())

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

# print(get_average_age_by_gender(df, "Male"))
# print(get_credit_score_from_greatest_balance(df))
