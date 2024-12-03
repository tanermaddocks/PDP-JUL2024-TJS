from typing import Any
from functions.basic import costForm, standardCalc, beerSize, recipePrint

class Beverage:
    # constructor
    def __init__ (self, date, code, name, alc, cost) -> None:
        self.date = date
        self.code = code
        self.name = name
        self.alc = alc
        self.cost = cost
        self.type = None
        self.serve = None
        self.mixed = False

    def get_item_date(self):
        return self.date

    def get_item_code(self):
        return self.code
    
    def get_item_name(self):
        return self.name
    
    def get_item_alc(self):
        return self.alc
    
    def get_item_cost(self):
        return self.cost
    
    def get_item_type(self):
        return self.type
        
    def get_item_serve(self):
        return self.serve

    def is_mixed(self):
        return self.mixed

class Beer(Beverage):
    def __init__(self, date, code, name, alc, cost, serve):
        super().__init__(date, code, name, alc, cost)
        self.type = "beer"
        self.serve = serve
    
    def __str__(self) -> str:
        return (f"\n {self.code} -> {self.name}"
                f"\n Type: {self.type.capitalize()}"
                f"\n Serve: {self.serve} ({beerSize(self.serve)}mL)"
                f"\n Alc/vol: {self.alc}% "
                f"({round(standardCalc(self.alc, beerSize(self.serve)), 2)} "
                f"standards)\n Cost: ${costForm(self.cost)}"
                f"\n Date added: {self.date}")


class Wine(Beverage):
    def __init__(self, date, code, name, alc, cost, serve):
        super().__init__(date, code, name, alc, cost)
        self.type = "wine"
        self.serve = serve

    def __str__(self) -> str:
        return (f"\n {self.code} -> {self.name}"
                f"\n Type: {self.type.capitalize()}"
                f"\n Serve: {self.serve}mL glass\n Alc/vol: {self.alc}% "
                f"({round(standardCalc(self.alc, self.serve), 2)} standards)"
                f"\n Cost: ${costForm(self.cost)}"
                f"\n Date added: {self.date}")


class Spirit(Beverage):
    def __init__ (self, date, code, name, alc, cost, subtype):
        super().__init__(date, code, name, alc, cost)
        self.subtype = subtype
        self.type = "spirit"
        self.serve = 30

    def __str__(self) -> str:
        return (f"\n {self.code} -> {self.name}"
                f"\n Type: {self.subtype.capitalize()} {self.type}"
                f"\n Serve: {self.serve}mL nip\n Alc/vol: {self.alc}% "
                f"({round(standardCalc(self.alc, self.serve), 2)} standards)"
                f"\n Cost: ${costForm(self.cost)}"
                f"\n Date added: {self.date}")
    
    def get_item_subtype(self):
        return self.subtype


class Mix(Beverage):
    def __init__(self, date, code, name, alc, cost, recipe):
        super().__init__(date, code, name, alc, cost)
        self.type = "mix"
        self.mixed = True
        self.recipe = recipe

    def __str__(self) -> str:
        return (f" {self.code} -> {self.name}"
                f"\n Type: {self.type.capitalize()}"
                f"\n Recipe: {recipePrint(self.recipe)}"
                f"\n Standard drinks: {round(self.alc, 2)}"
                f"\n Cost: ${costForm(self.cost)}"
                f"\n Date added: {self.date}")
    
    def get_mix_recipe(self):
        return self.recipe