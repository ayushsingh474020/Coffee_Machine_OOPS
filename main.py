from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

switch="On"
Maker=CoffeeMaker()
Machine=MoneyMachine()
item=Menu()
while (switch=="On"):
    Maker.report()
    items_list=item.get_items()
    coffee = input(f"What would you like? {items_list} ) : ")
    Item=item.find_drink(coffee)
    if(Item!=None):
      if(Maker.is_resource_sufficient(Item) and Machine.make_payment(Item.cost)):
        Maker.make_coffee(Item)
    switch=input("Switch (On/Off) : ")

print("GoodDay!!!")



