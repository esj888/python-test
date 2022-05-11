# how many squirrel per color
# build dataframe
# create csv called squirrel_count.csv


import pandas

squirrel_color = {}

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

color = data["Primary Fur Color"]
for x in color:
    # if x == "Gray":
    #    print("Gray found")
    if squirrel_color.get(x) is None:
        squirrel_color[x] = 1
    else:
        squirrel_color[x] += 1

print(squirrel_color)
print(list(squirrel_color.items()))
squirrel_df = pandas.DataFrame(list(squirrel_color.items()))
print(squirrel_df)
squirrel_df.to_csv("squirrel_count.csv")
