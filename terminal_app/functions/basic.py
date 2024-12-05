# Simple functions.

# random is an imported class that creates random data, the method used here is
# the randint method, which creates a random integer within the chosen parameters
import random

# mainMenu prints to the terminal the available options for the user to perform.
def mainMenu():
    print("\nWhat would you like to do?\n")
    print(" 1. Add stock.")
    print(" 2. Create a mix.")
    print(" 3. Search for a drink.")
    print(" 4. View drink lists.")
    print(" E. Exit application.")
    choice = str.lower(input("\nEnter your choice here: "))
    return choice
    # choice is returned as a string, where the accepted returned values are 
    # "1", "2", "3", "4" and "e", as determined by the match case in main.py.


# exitMessage is a simple print function, that is used in multiple cases.
def exitMessage():
    print("Thank for for using the cocktail reference application!")


# invalidEntry is a simple print function, that is used in multiple cases.
def invalidEntry():
    print("Invalid entry, try again.")


# exitMessage is a print function, that is used in multiple cases,
# where some require an additional option to make sense.
def wrongChoice(includeMix):
    if includeMix:
        print("Invalid item type, choose from beer, wine spirit or cocktail.")
    else:
        print("Invalid item type, choose from beer, wine or spirit.")


# capitalFullString takes a string, as an input and capitalises each word
# in the string, used for inputs from users to format them in standard way.
def capitalFullString(string):
    string_list = string.split()
    string_list_cap = []
    for word in string_list:
        string_list_cap.append(word.capitalize())
    string_cap = " ".join(string_list_cap)
    return string_cap
    # string_cap returns a string with the first letter of 
    # each word capitalised.


# codeMaker performs two essential task, it first creates a random code
# to be used as an item code, and then checks whether the code is in use,
# if it is, it produces a new random code until it finds one not in use.
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
    # returns a string in the format #001111, where the 1s can
    # be any integer.


# fileForm takes a string input and returns it back with no special
# characters, except "_" and no capital letters, it removes whitespace
# and any spaces become underscores, used to make bar names into file
# names that cause no error when saving them.
def fileForm(bar_name):
    bar_no_special = []
    for character in bar_name:
        if character not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"':
            bar_no_special.append(character.lower())

    bar_name_file = "_".join(("".join(bar_no_special)).split())
    return bar_name_file
    # returns a string with standard format to be used in file names


# valueErrorCheck is used to verify user inputs and reject any value
# that is unable to be converted into a number, used in many cases
# where only a number is desired as an input.
def valueErrorCheck(prompt):
    while prompt != " ":
        try:
            value = float(input(prompt))
            break
        except ValueError: 
            print("Must be a number, please try again.\n")
            continue
    return value
    # value returns a float value


# costForm is used to convert a regular float or integer value and
# change it into a string that displays a dollar value including cents
def costForm(cost):
    return "{:.2f}".format(cost)
    # returns a string that displays as a number with two decimal
    # places, even if the decimal values are 0.


# confirm asks a user to confirm their action, used in the case of item
# creation or deletion so as prevent accidental changes to files.
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
        # returns either boolean values to confirm an action or
        # returns an invalid entry message.


# standardCalc takes a percentage and vol value and calculates the
# australian standard drink value based on those values.
def standardCalc(alcpercent, vol): # unused as of now
    standard = ((alcpercent/100 * vol)/(10/0.78))
    # 10g is the standard drink in Australia 
    # and the density of alcohol is 0.78g/mL
    return standard
    # returns a float value that represents a standard drink amount


# beerSize takes the bar's standard beer serve size and returns the
# standard volume of the type of glass.
def beerSize(serve):
    match serve:
        case "pot": serve_mL = 285
        case "schooner": serve_mL = 425
        case "pint": serve_mL = 570
        case "stein": serve_mL = 1000
    return serve_mL
    # returns an integer value that represents a mL amount


# recipe print is used to produce a list of ingredients in a 
# mix in a different format to what the __str__ for the Beverage 
# class would othewise print.
def recipePrint(recipe_dict):
    print_list = []
    for item in recipe_dict:
        print_list.append(f"{item[0]}mL of {item[1]}")
    return print_list
    # returns a list of string values, is printed by another function