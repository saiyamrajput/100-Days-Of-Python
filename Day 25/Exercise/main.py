#
# # Using just file method to read csv file
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
#
# # Using csv library to read csv file
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
# # Using the pandas library to read csv file
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Getting Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Getting Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # Getting Row data value
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Creating a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# Central Park Squirrel Data Analysis

# import statement
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# stores total count of all three types of squirrels
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# printing the count of each squirrel type
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# creating dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# converting dictionary to dataframe and storing it in fle "squirrel_count.csv"
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
