from random import seed
from random import randint

# current day number
day = 1

# starting cash on hand
cash = 100.00

# coffee on hand (cups)
coffee = 100

# sales list of dictionaries
sales = [
    {
        "day": 1,
        "coffee_inv": 100,
        "advertising": "10",
        "temp": 68,
        "cups_sold": 16
    },
    {
        "day": 2,
        "coffee_inv": 84,
        "advertising": "15",
        "temp": 72,
        "cups_sold": 20
    },
    {
        "day": 3,
        "coffee_inv": 64,
        "advertising": "5",
        "temp": 78,
        "cups_sold": 10
    }
]

# empty sales list
sales = []

def welcome():
    print("Lets collect some information before we start the game.\n")
    
def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
    print("You have $" + str(cash_on_hand) + " cash on hand and the temperature is " + str(weather_temp) + ".")
    print("You have enough on hand to make " + str(coffee_inventory) + " cupes.\n")

def convert_to_float(s):
    # if conversion failes, assign 0 to it
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def get_weather():
    # generatte a random temperture between 20 and 90
    # We'll consider season later on, but this is good enough for now
    return randint(20, 90)

# run welcome message
welcome()

# get name and store name
name = prompt("What is your name?", True)
shop_name = prompt("What do you want to name your coffee shop?", True)

# We have what we need, so let's get started
print("\nOk, let's get started. Have fun!")

# The main game loop
running =  True
while running:
    # display the day and add a "fancy" text effect
    print("\n-----| Day " + str(day) + " @ " + shop_name + " |-----")
    
    temperature = get_weather()
    
    # display the cash and weather
    daily_stats(cash, temperature, coffee)
    
    # get price of a cup of coffee
    cup_price = prompt("What do you want to charge per cup of coffee?")
    
    # get price of a cup coffee
    print("\nYou can buy advertising to help prompt sales.")
    advertising = prompt("How much do you want to spend on advertising (0 for none)?", False)
    
    # convert advertising into a float
    advertising = convert_to_float(advertising)
    
    # deduct advertising from the cash on hand
    cash -= advertising
    
    #TODO: calculate today's performance
    cups_sold = prompt("How many cups of coffee were sold today?")
    profit = round(float(cup_price) * int(cups_sold), 2)
    #TODO: display today's performance
    print("\nToday's total profit: " + str(profit))
    
    # before we loop around, add a day
    day += 1
    
