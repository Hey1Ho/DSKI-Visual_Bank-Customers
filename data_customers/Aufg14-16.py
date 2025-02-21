from matplotlib.pylab import sqrt
import matplotlib.pyplot as plt
import pandas as pd
import os

csv_files = [f for f in os.listdir("./data_customers/data") if f.endswith('.csv')]
df_list = [pd.read_csv(os.path.join("./data_customers/data", file), delimiter="|") for file in csv_files]
df = pd.concat(df_list, ignore_index=True)


# Aufgabe 14
def aufg_14():
    customer_df = df[df["churn"] == 1]
    not_customer_df = df[df["churn"] == 0]

    fig, ax = plt.subplots()

    ax.scatter(customer_df["age"], customer_df["balance"], c="g", s=10, label="Kunde")
    ax.scatter(not_customer_df["age"], not_customer_df["balance"], c="r", s=10, label="kein Kunde mehr")
    ax.set_xlabel("Alter")
    ax.set_ylabel("Bilanz")
    ax.set_title("Zusammenhang Alter, Bilanz und Kundenstatus")
    ax.legend()
    ax.grid()
    plt.show()


# Aufgabe 15
def clean_gender(df):
    #entweder 'female' oder 'male'. Sonstiges wird auf den häufigsten Wert gesetzt (hier: 'male')
    df["gender"] = df["gender"].str.lower()
    df.loc[df["gender"] == "f", "gender"] = "female"
    df.loc[df["gender"] == "m", "gender"] = "male"
    df.loc[(df["gender"] != "male") & (df["gender"] != "female"), "gender"] = df["gender"].value_counts().idxmax() #idxmax: gibt den Index des Maximums zurück
    return df

# Aufgabe 16
def kick_unecessary_columns(df):
    df = df.drop(columns=['num_kids'])  # num_kids hat nur einen Wert
    return df

# Aufgabe 17
def histogram_balance():
    fig, ax = plt.subplots(1,1, figsize=(6,4))
    # bins = int(sqrt(abs(df["balance"].min())+abs(df["balance"].max())))
    # print(abs(df["balance"].min())+abs(df["balance"].max()), " Range")
    # print(bins, " Bins") #-> 500 bins
    ax.hist(df["balance"], bins=40, edgecolor="black")
    # ax vertical line
    ax.axvline(df["balance"].median(), color="orange", label="Kontostand")

    ax.set_title("Verteilung des Kontostands")
    ax.set_ylabel("Häufigkeit")
    ax.set_xlabel("Kontostand (US$)")
    ax.tick_params(axis='x', labelrotation=45)
    ax.legend()
    plt.tight_layout()
    plt.show()

# Aufgabe 18
def histogram_boxplot_combined_germany():
    fig, ax = plt.subplots(2,1, figsize=(6,4))
    ax[0].hist(df.loc[df["country"]=="Germany", "balance"], bins=40, edgecolor="black")
    # ax vertical line
    ax[0].axvline(df.loc[df["country"]=="Germany", "balance"].median(), color="orange", label="Kontostand")

    ax[0].set_title("Verteilung des Kontostands in DE")
    ax[0].set_ylabel("Häufigkeit")
    ax[0].set_xlabel("Kontostand (US$)")
    ax[0].tick_params(axis='x', labelrotation=45)
    ax[0].legend()

    ax[1].boxplot(df["balance"].fillna(df.loc[df["country"]=="Germany", "balance"].median()), vert=False)
    ax[1].set_yticklabels(["Kontostand"], rotation=90)
    ax[1].set_xlabel("Alter")
    plt.tight_layout()
    plt.show()





aufg_14()
df = clean_gender()
df = kick_unecessary_columns(df)
print(df.describe(include="all"))
histogram_balance()
histogram_boxplot_combined_germany()
