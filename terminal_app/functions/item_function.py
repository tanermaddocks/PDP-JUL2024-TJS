import datetime
from classes.stock import Beer, Wine, Spirit, Mix
from functions.basic import capitalFullString, valueErrorCheck,\
                            confirm, wrongChoice, costForm, codeMaker, \
                            standardCalc
from functions.file_function import saveFile


# Add stock
def addStock(bar):
    print("\nADDING NEW STOCK")
    # date added
    
    date = str(datetime.date.today())

    # generate item code for new item
    code = codeMaker(bar)
 
    # ask for item type being added
    item_type = str.lower(input(
        "What item do you wish to add; beer, wine or spirit? "))
    match item_type:
        case "beer": pass
        case "wine": pass
        case "spirit": pass
        case _: return wrongChoice(False)
    
    # item name
    name = capitalFullString(input(f"What is the name of the {item_type}? "))

    # item strength in percent
    alc = valueErrorCheck(f"What is the alcohol percentage of {name}? ")

    # insert into a class relevant to type
    match item_type:
        # for beer
        case "beer": 
            beer_serve = bar.get_beer_serve()
            #item cost
            cost = valueErrorCheck(f"How much does {name} cost "
                                   f"for a {beer_serve}? ")
            new_item = Beer(date, code, name, alc, cost, beer_serve)
        # for wine
        case "wine": 
            wine_serve = bar.get_wine_serve()
            #item cost
            cost = valueErrorCheck(f"How much does {name} cost for "
                                   f"a {wine_serve}mL glass? ")
            new_item = Wine(date, code, name, alc, cost, wine_serve) 
        # for spirit
        case "spirit": 
            subtype = str.lower(input(f"What kind of spirit is {name}?"
                                      "\n - Vokda\n - Tequila\n - Rum\n - Gin"
                                      "\n - Whiskey\n - Brandy\n - Liqueur"
                                      "\nEnter one of the above options: "))
            cost = valueErrorCheck(f"How much does {name} "
                                   f"cost for a 30ml nip? ")
            new_item = Spirit(date, code, name, alc, cost, subtype)    
    
    # add item to bar dictionary
    print(f"\n{new_item}")
    print(f"\nAdd {name} to {bar}'s menu?")
    approve = confirm()
    if approve:
        bar.add_item(new_item)
        saveFile(bar)
    else:
        print("Add item cancelled.")


# Add mix
def addMix(bar):
    print("\nADDING NEW MIX")
    date_added = str(datetime.date.today())
    mix_code = codeMaker(bar)
    mix_name = capitalFullString(input("What is the name of your mix? "))
    # ask for drink 1 through to drink x
    print(f"Enter your the ingredients of a {mix_name} "
          "and the quantity (in mL) of each ingredient.\n")
    recipe = []
    x = 0
    while x != 1:
        ingredient = bar.search_item(
            bar, f"Enter the name or code of a stock item: ")
        if not ingredient:
            print ("No item in menu with that code or name.")
        elif ingredient.is_mixed():
            print ("Can not have a mix as an ingredient for a mix.")
        else:
            ing_vol = int(valueErrorCheck(
                f"How many mL of {ingredient.get_item_name()} are in "
                f"a {mix_name}? "))               # volm [0]
            ing_name = ingredient.get_item_name() # name [1]
            ing_alc = ingredient.get_item_alc()   # alc% [2]
            ing_cost = ingredient.get_item_cost() # cost [3]
            recipe.append([ing_vol, ing_name, ing_alc, ing_cost])
            print (f"{ing_vol}mL of {ing_name} added.")
        print("\nAdd another ingredient?")
        answer = confirm()
        if not answer:
            x += 1
    if mix_name[0] in "AEIOU":
        print(f"\nRecipe for an {mix_name}:")
    else:
        print(f"Recipe for a {mix_name}:")
    mix_alc = 0
    total_cost = 0
    mix_recipe = []
    for ingr in recipe:
        mix_recipe.append((ingr[0], ingr[1]))
        print(f" - {ingr[0]}mL of {ingr[1]}")
        # add together the standard drinks of each item
        mix_alc += standardCalc(ingr[2], ingr[0])
        total_cost += ingr[3]
    print(f"Contains {round(mix_alc, 2)} standards.\n"
            f"\nA {mix_name} would usually cost ${costForm(total_cost)}.")
    
    # ask for a price (display combined sale price of all mixed items)    
    mix_cost = valueErrorCheck("What is the new cost? ")

    # print new combined item (include ingredients)
    new_mix = Mix(date_added, mix_code, mix_name, mix_alc, mix_cost, mix_recipe)

    # add item to bar dictionary
    print(f"\n{new_mix}")
    print(f"\nAdd {mix_name} to {bar}'s menu?")
    approve = confirm()
    if approve:
        bar.add_item(new_mix)
        saveFile(bar)
    else:
        print("Add item cancelled.")


# Search for an item
def searchItem(bar):
    print("\nSEARCHING MENU")
    searched_item = bar.search_item(
        bar, "Enter the code or name of the item you are searching for: ")
    if not searched_item:
        return print ("No item in menu with that code or name.")
    print(searched_item)
    search_item_name = searched_item.get_item_name()
    search_item_code = searched_item.get_item_code()
    choice = ""
    while choice != "e":
        choice = str.lower(input(f"\nEnter E to return to the main menu or "
                                 f"enter D to delete {search_item_name} "
                                 f"from {bar}'s menu: "))
        if choice == "d":
            # confirm delete
            print(f"Delete {search_item_code} -> {search_item_name} "
                  f"from {bar}'s menu?")
            approve = confirm()
            if approve:
                bar.delete_item(search_item_code)
                saveFile(bar)
            else: 
                print("Delete item cancelled.")
            break


# List items
def listItem(bar):
    print("\nVIEWING MENU")
    all_items = bar.get_items()
    if not all_items: 
        return print("No items in bar.")
    print("Which items would you like to see?")
    type = str.lower(input("Choose from beer, wine, spirit, mix or all: "))
    print()
    for item in all_items: 
        printList = (f" {item.get_item_code()} -> {item.get_item_name()}"
                     f" - ${costForm(item.get_item_cost())}")
        match type:
            case "beer":
                # see beer
                if item.get_item_type() == "beer": print(printList)
            case "wine":
                # see wine
                if item.get_item_type() == "wine": print(printList)
            case "spirit":
                # see spirit
                if item.get_item_type() == "spirit": print(printList)
            case "mix": 
                # see mix
                if item.get_item_type() == "mix": print(printList)
            case "all":
                # see all
                print(printList)
            case _:
                # wrong input
                wrongChoice(True)