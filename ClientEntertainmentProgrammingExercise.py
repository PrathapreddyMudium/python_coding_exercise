import sys
import pandas as pd


def basket_analysis(filename):
    df = pd.read_csv(filename)

    # print(df)
    # 1st Question
    df_size = df["size"]
    total_number_of_fruit = 0
    for item in df_size:
        total_number_of_fruit += item
    print(total_number_of_fruit)

    # 2nd Question
    df_name = df["name"].unique()
    print(df_name.size)

    # 3rd Question
    df_size_sort = df.groupby("name").sum().sort_values("size", ascending=False)
    print(df_size_sort.iloc[:, 0:1])

    # 4th question
    df_characterstics = df.groupby(["name", "color", "shape"]).agg({"size": ["sum"]})
    df_characterstics.columns = ["sum"]
    df_characterstics = df_characterstics.reset_index()
    # print(df_characterstics)
    for index, row in df_characterstics.iterrows():
        print(str(row["sum"]) + " " + row["name"] + ":" + row["color"] + "," +
              row["shape"])

    # 5th Question
    df_3days = df.loc[df["days"] > 3]
    df_3days = df_3days.drop_duplicates()
    for index, row in df_3days.iterrows():
        print(str(row["size"])+" "+row["color"]+" "+row["shape"] + " "+row["name"] + " are "+str(row["days"]) + "days "
                                                                                                                "old")
    # for item2 in df_3days


basket_analysis(sys.argv[1])
