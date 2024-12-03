from functions.basic import capitalFullString, invalidEntry, valueErrorCheck

class Bar:
    def __init__(self, name, beer_serve, wine_serve):
        self.name = name
        self.beer_serve = beer_serve
        self.wine_serve = wine_serve
        self.items = []
        
    def __str__(self) -> str:
        name = self.name.split("_")
        name = " ".join(name)
        name = capitalFullString(name)
        return name
    
    def get_name(self):
        return self.name

    def get_beer_serve(self):
        return self.beer_serve
    
    def set_beer_serve(self, beer_serve):
        self.serve = beer_serve

    def get_wine_serve(self):
        return self.wine_serve
    
    def set_wine_serve(self, wine_serve):
        self.serve = wine_serve

    def add_item(self, new_item):
        self.items.append(new_item)

    def search_item(self, bar, prompt):
        target = str(input(prompt))
        # find item code and name
        if target[:2] == "00":
            target = "#" + target
        all_items = bar.get_items()
        for item in all_items:
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

    def delete_item(self, item_code):
        new_menu = []
        deleted = False
        for item in self.items:
            if item.get_item_code() != item_code:
                new_menu.append(item)  
            else: deleted = True
        self.items = new_menu
        return deleted

    def get_items(self):
        return self.items