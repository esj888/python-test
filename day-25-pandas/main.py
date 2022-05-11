# import fileinput
#
#
# def load_data():
#     with open("weather_data.csv") as data:
#         weather_data = data.readlines()
#     print(weather_data)
#
#
# load_data()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#             print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(round(avg_temp, 1))

# or use pandas mean method
print(round(data["temp"].mean(), 1))

max_temp = data["temp"].max()
print(max_temp)

# get data in row
print(data[data.day == "Monday"])

# print row with highest temp
print(data[data.temp == data["temp"].max()])

# monday's condition
monday = data[data.day == "Monday"]
print(monday.condition)
temp_f = (int(monday.temp) * 1.8) + 32
print("Monday in Fahrenheit = ", temp_f)

# create data frame and a csv file from that data frame
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_data.csv")



