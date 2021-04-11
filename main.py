# Python Cheat Sheet

#list Comprehension
#new_list = [new_item for item in list if test
#newlist = [expression for item in iterable if condition == True]
#newlist = [x if x != "banana" else "orange" for x in fruits]
#"Return the item if it is not banana, if it is banana return orange".
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]  #if
#loop Through list items
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#loop through list index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#dict Comprehension
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}
#              {key: value for (key, value) in iterable}
squares = {x: x*x for x in range(6)} #if
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#This code is equivalent to
squares2 = {}
for x in range(6):
    squares2[x] = x*x
#loop through dictionaries:
for(key, value) in dict.items():
    print(value)

#turn string into dict by words and counts len
sentence = "What is the Airspeed Velocity of an unladen Swallow?"
result = {word: len(word) for word in sentence.split()}

#Read csv files
#import csv
#with open("Squirrel_Data.csv") as data_file:
#    data = csv.reader(data_file)
#    for row in data:
#        print(row)


#turn string into a list
str1 = "Python pool for python knowledge"
list1 = list(str1)
print(list1)
