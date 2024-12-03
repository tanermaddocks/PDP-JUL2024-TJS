import json 
import os
from classes.bar import Bar
from classes.stock import Beer, Wine, Spirit, Mix
from functions.basic import valueErrorCheck, confirm, \
                            exitMessage, invalidEntry


def saveFile(bar):
    barname = bar.get_name()
    #info save
    try: 
        os.mkdir(f"data")
    except FileExistsError: 
        pass
    try: 
        os.mkdir(f"data/{barname}")
    except FileExistsError: 
        pass
    bar_info = {
        "barname": bar.get_name(),
        "beerserve": bar.get_beer_serve(),
        "wineserve": bar.get_wine_serve()
        }
    with open(f"data/{barname}/{barname}_info.json", "w") as json_file:
        json.dump(bar_info, json_file, indent=4)
    #menu save
    item_dict = []
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
    with open(f"data/{barname}/{barname}_menu.json", "w") as json_file:
        json.dump(item_dict, json_file, indent=4)
    print("Bar menu updated.")


def loadInfo(barname):
    try:
        #info load
        with open(f"data/{barname}/{barname}_info.json", "r") as json_file:
            bar_info = json.load(json_file)
            barname = bar_info["barname"]
            beerserve = bar_info["beerserve"]
            wineserve = bar_info["wineserve"]
        return Bar(barname, beerserve, wineserve)
    except FileNotFoundError:
        print("\nBar not on file, do you want to add a new bar?")
        approve = confirm()
        if approve:
            print("\nWhat does your bar use as "
                  "a standard beer and wine serve?")
            x = 0
            while x == 0:
                standard_beer_serve = input(
                    "Choose one of pot, schooner, pint or stein: ")
                match standard_beer_serve:
                    case "pot": break
                    case "schooner": break
                    case "pint": break
                    case "stein": break
                    case _: invalidEntry
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
        #menu load
        with open(f"data/{barname}/{barname}_menu.json", "r") as json_file:
            item_dict = json.load(json_file)
            for item in item_dict:
                date = item["date"]
                code = item["code"]
                name = item["name"] 
                alc = item["alc"]
                cost = item["cost"]
                type = item["type"]
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
    