# Simple functions.

import random

def mainMenu():
    print("\nWhat would you like to do?\n")
    print(" 1. Add stock.")
    print(" 2. Create a mix.")
    print(" 3. Search for a drink.")
    print(" 4. View drink lists.")
    print(" E. Exit application.")
    choice = str.lower(input("\nEnter your choice here: "))
    return choice

def exitMessage():
    print("Thank for for using the cocktail reference application!")

def invalidEntry():
    print("Invalid entry, try again.")

def wrongChoice(includeMix):
    if includeMix:
        print("Invalid item type, choose from beer, wine spirit or cocktail.")
    else:
        print("Invalid item type, choose from beer, wine or spirit.")

def capitalFullString(string):
    string_list = string.split()
    string_list_cap = []
    for word in string_list:
        string_list_cap.append(word.capitalize())
    string_cap = " ".join(string_list_cap)
    return string_cap

def codeMaker(bar):
    # generate item code
    all_items = bar.get_items()
    # check code does not already exist
    existing_codes = []
    for item in all_items:
        existing_codes.append(item.get_item_code())
    x = 0
    while x == 0:
        code = format(random.randint(0, 9999), "06d")
        if code not in existing_codes: x += 1
    return f"#{code}"

def fileForm(bar_name):
    bar_no_special = []
    for character in bar_name:
        if character not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"':
            bar_no_special.append(character.lower())

    bar_name_file = "_".join(("".join(bar_no_special)).split())
    return bar_name_file

def valueErrorCheck(prompt):
    while prompt != " ":
        try:
            value = float(input(prompt))
            break
        except ValueError: 
            print("Must be a number, please try again.\n")
            continue
    return value

def costForm(cost):
    return "{:.2f}".format(cost)

def confirm():
    answer = ""
    while answer != "yes" and answer != "no":
        answer = str.lower(input(
            "Enter 'yes' to confirm, or 'no' to cancel: "))
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else: invalidEntry()

def standardCalc(alcpercent, vol): # unused as of now
    standard = ((alcpercent/100 * vol)/(10/0.78))
    # 10g is the standard drink in Australia 
    # and the density of alcohol is 0.78g/mL
    return standard

def beerSize(serve): # unused as of now
    match serve:
        case "pot": serve_mL = 285
        case "schooner": serve_mL = 425
        case "pint": serve_mL = 570
        case "stein": serve_mL = 1000
    return serve_mL

def recipePrint(recipe_dict):
    print_list = []
    for item in recipe_dict:
        print_list.append(f"{item[0]}mL of {item[1]}")
    return print_list