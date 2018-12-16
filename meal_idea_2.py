## Program Name: meal_idea.py
## Author: Brian K. Vagnini
## Started 10/18/18
##
## Description:
## This program helps me to select from five JSON files, each
## containing a component of a full meal.
## This is to assist me when I get stuck for meal ideas.

import json
from pprint import pprint

#load the json file from user input
print (""" Choose a number from the following:
1 = main_dish
2 = bread
3 = sauce
4 = starch
5 = vegetable""")

##1 = "main_dish.json"
##2 = "bread.json"
##3 = "sauce.json"
##4 = "starch.json"
##5 = "vegetable.json"

json_file = input()

print ("You selected " + json_file)

f = "0"
if json_file == "1":
    f = "main_dish.json"
    print ("You selected " + f)
elif json_file == "2":
    f = "bread.json"
    print ("You selected " + f)
elif json_file == "3":
    f = "sauce.json"
    print ("You selected " + f)
elif json_file == "4":
    f = "starch.json"
    print ("You selected " + f)
elif json_file == "5":
    f = "vegetable.json"
    print ("You selected " + f)
else:
    print ("PLease choose a number between 1 and 5 or Ctrl + C to exit")

#below portion currently doesn't work properly    
#with open (f) as file:
data = json.load(f,r)
print (data)
    
# select random value from the array
random_value = random(data) in data.length
print (random_value)
#meal_idea = data["beef"][random_value]["id"]

#pprint (meal_idea)
