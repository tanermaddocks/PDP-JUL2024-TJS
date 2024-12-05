# json is an inbuilt class that is imported to provide management of json
# documents so that the application can write and read from the json docs
# in the data directory
import json 
# os is an inbuilt class that allows the program to create directories
# which in this program is used to manage multiple bars
import os

from classes.bar import Bar
from classes.stock import Beer, Wine, Spirit, Mix
from functions.basic import valueErrorCheck, confirm, \
                            exitMessage, invalidEntry


# used to either create or writeover a json file, will also create the data
# and child directories if they do not exist already
def saveFile(bar):
    barname = bar.get_name()
    #creates directory if not already existing
    try: 
        os.mkdir(f"terminal_app/data")
    except FileExistsError: 
        pass
    try: 
        os.mkdir(f"terminal_app/data/{barname}")
    except FileExistsError: 
        pass
    #creates a dictionary for the bar info
    bar_info = {
        "barname": bar.get_name(),
        "beerserve": bar.get_beer_serve(),
        "wineserve": bar.get_wine_serve()
        }
    #opens the json file and dumps bar_info into it
    with open(f"terminal_app/data/{barname}/{barname}_info.json", "w") as json_file:
        json.dump(bar_info, json_file, indent=4)
    #creates an empty dict for the bar menu
    item_dict = []
    #loops through all the different drinks and then if it matches the type of drink it will add the info
    #appropriate to that drink type to the dict
    for item in bar.get_items():
        if item.get_item_type() == "beer":
            item_json = {
                "date": item.get_item_date(),
                "code": item.get_item_code(),
                "name": item.get_item_name(),
                "alc": item.get_item_alc(),
                "cost": item.get_item_cost(),
                "type": item.get_item_type(),
                "serve": item.get_item_serve(),
                "mixed": item.is_mixed()
            }
        elif item.get_item_type() == "wine":
            item_json = {
                "date": item.get_item_date(),
                "code": item.get_item_code(),
                "name": item.get_item_name(),
                "alc": item.get_item_alc(),
                "cost": item.get_item_cost(),
                "type": item.get_item_type(),
                "serve": item.get_item_serve(),
            }
        elif item.get_item_type() == "spirit":
            item_json = {
                "date": item.get_item_date(),
                "code": item.get_item_code(),
                "name": item.get_item_name(),
                "alc": item.get_item_alc(),
                "cost": item.get_item_cost(),
                "type": item.get_item_type(),
                "stype": item.get_item_subtype(),
                "serve": item.get_item_serve()
            }
        elif item.get_item_type() == "mix":
            item_json = {
                "date": item.get_item_date(),
                "code": item.get_item_code(),
                "name": item.get_item_name(),
                "alc": item.get_item_alc(),
                "cost": item.get_item_cost(),
                "type": item.get_item_type(),
                "recipe": item.get_mix_recipe()
            }
        item_dict.append(item_json)
    #opens the json file and dumps item_dict into it
    with open(f"terminal_app/data/{barname}/{barname}_menu.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)
    print("Bar menu updated.")


def loadInfo(barname):
    try:
        #open the barname info json file and if the file doesnt exist prompts
        #the user to add a new bar
        with open(f"terminal_app/data/{barname}/{barname}_info.json", "r") as json_file:
            bar_info = json.load(json_file)
            barname = bar_info["barname"]
            beerserve = bar_info["beerserve"]
            wineserve = bar_info["wineserve"]
        return Bar(barname, beerserve, wineserve)
    except FileNotFoundError:
        print("\nBar not on file, do you want to add a new bar?")
        approve = confirm()
        #verifies user wants to add a new bar
        if approve:
            print("\nWhat does your bar use as "
                  "a standard beer and wine serve?")
            x = 0
            while x == 0:
                standard_beer_serve = input(
                    "Choose one of pot, schooner, pint or stein: ")
                #makes sure the user enters valid input and then breaks the loop if so or else throws error invalidEntry
                match standard_beer_serve:
                    case "pot": break
                    case "schooner": break
                    case "pint": break
                    case "stein": break
                    case _: invalidEntry
            #converts user input to int
            standard_wine_serve = int(valueErrorCheck(
                "Volume of a standard wine glass (in mL): "))
            return Bar(barname, standard_beer_serve, standard_wine_serve)
        else:
            print()
            exitMessage()
            exit()


def loadMenu(bar):
    barname = bar.get_name()
    try:
        #attemps to load the menu json file
        with open(f"terminal_app/data/{barname}/{barname}_menu.json", "r") as json_file:
            item_dict = json.load(json_file)
            for item in item_dict:
                date = item["date"]
                code = item["code"]
                name = item["name"] 
                alc = item["alc"]
                cost = item["cost"]
                type = item["type"]
                #matches the type from the json file to the correct drink type
                match type:
                    case "beer":
                        serve = item["serve"]
                        item = Beer(date, code, name, alc, cost, serve)
                    case "wine":
                        serve = item["serve"]
                        item = Wine(date, code, name, alc, cost, serve)
                    case "spirit": 
                        subtype = item["stype"]
                        item = Spirit(date, code, name, alc, cost, subtype) 
                    case "mix": 
                        recipe = item["recipe"]
                        item = Mix(date, code, name, alc, cost, recipe)
                bar.add_item(item)
    except FileNotFoundError: pass
    