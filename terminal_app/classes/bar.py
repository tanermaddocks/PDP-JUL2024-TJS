from functions.basic import capitalFullString

class Bar:
    # initialises the bar class
    def __init__(self, name, beer_serve, wine_serve):
        self.name = name
        self.beer_serve = beer_serve
        self.wine_serve = wine_serve
        self.items = []

    #if bar is called it will return the following string
    def __str__(self) -> str:
        name = self.name.split("_")
        name = " ".join(name)
        name = capitalFullString(name)
        return name
    	
    #returns the name of the bar
    def get_name(self):
        return self.name

    #returns the serve of the beer
    def get_beer_serve(self):
        return self.beer_serve
    
    #sets the serve of the beer
    def set_beer_serve(self, beer_serve):
        self.serve = beer_serve

    #returns the serve of the wine
    def get_wine_serve(self):
        return self.wine_serve
    
    #sets the serve of the wine
    def set_wine_serve(self, wine_serve):
        self.serve = wine_serve

    #adds a new item to the bar
    def add_item(self, new_item):
        self.items.append(new_item)

    #searches for an item in the bar
    def search_item(self, bar, prompt):
        target = str(input(prompt))
        # find item code and name
        if target[:2] == "00":
            target = "#" + target
            #  properly formats user input
        all_items = bar.get_items()
        for item in all_items:
            # searches by name or item code
            if target[0] == "#":
                if item.get_item_code() == target:
                    return item
            else:
                target = capitalFullString(target)
                if item.get_item_name() == target:
                    return item
        # if none found
        else: 
            return False
            # return either a boolean or the item object

    # deletes an item from the bar using its item code
    def delete_item(self, item_code):
        new_menu = []
        deleted = False
        for item in self.items:
            if item.get_item_code() != item_code:
                new_menu.append(item)  
            else: deleted = True
        self.items = new_menu
        return deleted
        # return a boolean value which is used to confirm deletion

    # used to retrieve all items
    def get_items(self):
        return self.items
        # return full item dictionary