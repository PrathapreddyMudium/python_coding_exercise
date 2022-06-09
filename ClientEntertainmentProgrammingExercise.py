import sys
import pandas as pd


def basket_analysis(filename):
    df = pd.read_csv(filename)

    # print(df)
    # 1st Question
    print("XXXXXX===== Total number of fruit: =====XXXXXX")
    df_size = df["size"]
    total_number_of_fruit = 0
    for item in df_size:
        total_number_of_fruit += item
    print("Total number of fruits: " + str(total_number_of_fruit))

    # 2nd Question
    print("XXXXXX===== Types of fruit: =====XXXXXX")
    df_name = df["name"].unique()
    print("Types of fruit: " + str(df_name.size))

    # 3rd Question
    print("XXXXXX===== The number of each type of fruit in descending order: =====XXXXXX")
    df_size_sort = df.groupby("name").sum().sort_values("size", ascending=False)
    print(df_size_sort.iloc[:, 0:1])

    # 4th question
    print('XXXXXX===== The characteristics (size, color, shape, etc.) of each fruit by type: =====XXXXXX')
    df_characterstics = df.groupby(["name", "color", "shape"]).agg({"size": ["sum"]})
    df_characterstics.columns = ["sum"]
    df_characterstics = df_characterstics.reset_index()
    # print(df_characterstics)
    for index, row in df_characterstics.iterrows():
        print(str(row["sum"]) + " " + row["name"] + ":" + row["color"] + "," +
              row["shape"])

    # 5th Question
    print("XXXXXX===== Have any fruit been in the basket for over 3 days: =====XXXXXX")
    df_3days = df.loc[df["days"] > 3]
    df_3days = df_3days.drop_duplicates()
    for index, row in df_3days.iterrows():
        print(str(row["size"])+" "+row["color"]+" "+row["shape"] + " "+row["name"] + " are "+str(row["days"]) + " days "
                                                                                                                "old")
    # for item2 in df_3days


basket_analysis(sys.argv[1])
