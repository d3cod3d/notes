
import pandas
data = pandas.read_csv("Squirrel_Data.csv")
#the begining and the end of the first and last lines
#gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
#print(gray_squirrels)
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#print(gray_squirrels_count)
data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
#make a csv file from data
#new_data_frame = pandas.DataFrame(data_dict)
#new_data_frame.to_csv("squirrel_count.csv")
#print(("Made Squirrel_Count.csv"))

#make panda data frame from dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame
#for(key,value) in student_data_frame.items():
#    print(value)

#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}