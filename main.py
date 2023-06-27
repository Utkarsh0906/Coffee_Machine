from Menu import MENU
from Resources import Resources
from MoneyReceived import total_amount
from os import system
from time import sleep
from Sufficient_Resource import sufficient_resource
while(True):
    system("cls")
    print("Welcome!!\nWhat coffee would you like??")
    call = input("Enter 'E' for Espresso, 'L' for Latte, and 'C' for Cappuccino: ").upper()
    if(call == 'E'):
        coffee = MENU['espresso']
    elif(call == 'L'):
        coffee = MENU['latte']
    elif(call == 'C'):
        coffee = MENU['cappuccino']
    elif(call == 'OFF'):
        print("Coffee machine closing down")
        break
    elif(call == "REPORT"):
        print(f"Resources available are:\nWater: {Resources['water']}\nMilk: {Resources['milk']}\nCoffee: {Resources['coffee']}\nMoney: {Resources['money']}")
        continue
    sleep(1)
    if(not(sufficient_resource(Resources,coffee))):
        continue
    print(f"The cost of your coffee is Rs. {coffee['cost']}")
    print("Please enter money")
    total = total_amount()
    sleep(1)
    if(total<coffee['cost']):
        print("Sorry insufficient funds. Money Refunded")
        continue
    elif(total>coffee['cost']):    
        print(f"Here's the extra money: Rs. {total-coffee['cost']}")
    sleep(1)
    print("Here's your coffee")
    Resources['water'] -= coffee['water'] 
    Resources['milk'] -= coffee['milk'] 
    Resources['coffee'] -= coffee['coffee']
    Resources['money'] += coffee['cost'] 
    sleep(3)    