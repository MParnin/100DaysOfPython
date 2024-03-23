# import csv

# with open("Projects/Day 025 - US States Game/weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("Projects/Day 025 - US States Game/weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data.temp.max())

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
# print(monday.condition)

# data_dict = {
#     "students": ["Amy", "James", "Angela"], 
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("Interactive Exercises/Day 025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240320.csv")

gray = data["Primary Fur Color"].value_counts()["Gray"]
cinnamon = data["Primary Fur Color"].value_counts()["Cinnamon"]
black = data["Primary Fur Color"].value_counts()["Black"]

count_dict = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Counts": [gray, cinnamon, black]
}

df = pandas.DataFrame(count_dict)

df.to_csv("Interactive Exercises/Day 025/squirrl_color.csv")