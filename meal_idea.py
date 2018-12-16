## Program Name: meal_idea.py
## Author: Brian K. Vagnini
## Started 10/18/18 Revised 12/16/18
##
## Description:
## This program helps me to select from three to five tuples (phase 1) (five JSONt files - phase 2), each
## containing a component of a full meal.
## This is to assist me when I get stuck for meal ideas.

import random

main = ("Steak","Cube Steak","Beef Tips","Hamburger","Beef Pot Roast","Meat Loaf",
        "Pork Chop (baked)","Pork Chop (Fried)","Ham Slice","Bacon","Pork Roast",
        "Italian Sausage","Smoked Sausage",
        "Chicken Tenders/Nuggets","Whole Roasted Chicken","Baked Chicken (Thighs, Wings, Legs)",
	"Air-Fried Chicken (Thighs, Wings, Legs)","Fried Chicken","Cornish Game Hens",
	"Chicken-n-Waffles","Scrambled Eggs","Fried Eggs","Chicken Quesadillas",
        "Baked Fish","Grilled/Pan Fried Fish","Fried Catfish","Fried Shrimp",
	"Boiled Shrimp","Grilled Shrimp","Crab","Lobster Tail","Tuna","Salmon Croquets",
	"Fish Tacos",
        "PB-n-J","Open Faced Tomatoe, Bacon, and Mushroom","Open Faced Manwiches",
	"Grilled Cheese/Tomato Soup","BLT","Pineapple & Cheese Sandwich","Peanut Butter & Banana Sandwich",
	"BBQ Sandwich",
        "Homemade Hamburger Helper (HHH)","Cheesy Rotele Chicken & Rice (CRx2)",
        "Breakfast","Lasagna","Chili Cheese Dogs","Corn Dogs")

starch = ("Baked Potato","Tator Tots","French Fries","Sweet Potato Fries","Mashed Potatos",
	"White Rice","Yellow Rice",
        "Egg Noodles","Ramen Noodles","Spaghetti Noodles","Macaroni","Bow Ties",
        "Spirals","Shells","Mac-n-Cheese",
        "Cheese Grits","Grits")

vegetable = ("Green Beans","Lima Beans","Navy Beans","Pinto Beans","Black Beans",
          "Shelly Beans","Green Sweet Peas","Black Eyed Peas",
          "Corn","Corn on the Cob","Creamed Corn",
          "Yellow Squash/Onions","Fried Breaded Squash","Squash/Zuccini/Mushrooms",
          "Tomato Slices","Fried Green Tomatoes","Tomatoes and Okra",
          "Raw Cabbage","Boiled Cabbage","Steamed Cabbage",
          "Fried Okra","Mushrooms","Salad","Eggplant Fritters","Carrots",
          "Cauliflower (Garlic Roasted)","Onions/Peppers","Broccoli")


while True:
    main_dish = random.choice(main)
    starch_side = random.choice(starch)
    veggie_side = random.choice(vegetable)

    print ("\n\n\tHow about {} with {} and {}\n\n".format(main_dish, starch_side,veggie_side))
    try_again = input("Try again? Enter for try again, n to quit: ")
    if try_again.lower() == "n":
        break
    input ("Press Enter to try another suggestion.") 
           




