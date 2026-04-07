import random
import re
import numpy
from utilities import *

class CoffeeShopSimulator:
    
    # Minimun and maximum temperature
    TEMP_MIN = 20
    TEMP_MAX = 90
    
    # length of temperature list
    # higher for more realistic curve
    SERIES_DENSITY = 300
    
    def __init__(self, player_name, shop_name):
        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name
        
        # Current day number
        self.day = 1
        # Cash on hand at start
        self.cash = 100.00
        # Inventory at start
        self.coffee_inventory = 100
        # Sales lit
        self.sales = []
        # Possible temperature
        self.temps = self.make_temp_distribution()
    
    def run(self):
        print("\nOk, let's get started. Have fun!")
        
        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text effect
            self.day_header()
            
            # Get the weather
            temperature = self.weather
            
            # Display the cash and weather
            self.daily_stats(temperature)
            
            # Get price of a cup of coffee
            # cup_price = float(prompt("What do you want to charge per cup of coffee?"))
            response = prompt("What do you want to charge per cup of coffee? (type exit to quit)")
            if re.search("^exit", response, re.IGNORECASE):
                running = False
                continue
            else:
                cup_price = float(response)
                
            # do you want to buy more inventory
            response = prompt("Do you want to buy more coffee for your inventory? (hit enter for none or type number)", False)
            
            if response:
                if not self.buy_coffee(response):
                    print("Could not buy additional inventory.")
            
            # Get advertising spend
            print("\nYou can buy advertising to help promote sales.")
            advertising = prompt("How much do you wan to spend on advertising (0 for none)?", False)
            
            # Convert advertising into a float
            advertising = convert_to_float(advertising)
            
            # Deduct advertising from cash on hand
            self.cash -= advertising
            
            #Simulate today's sales
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price
            
            # Display the results
            print("You sold " + str(cups_sold) + " cups of coffee today")
            print("You made $" + str(gross_profit) + ".")
            
            # Add the profit to oue coffers
            self.cash += gross_profit
            
            # Subtract inventory
            self.coffee_inventory -= cups_sold
            
            # check cash on hand
            if self.cash < 0:
                print("\n:( Game over! you ran out of cash.")
                running = False
                continue
            
            # Before we loop around, add a day
            self.increment_day()
    
    def simulate(self, temperature, advertising, cup_price):
        # Find out how many cups were sold
        cups_sold = self.daily_sales(temperature, advertising, cup_price)
        
        # Save the sales data for today
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })
        
        return cups_sold
    
    def buy_coffee(self, amount):
        try:
            i_amount = int(amount)
        except ValueError:
            return False
        
        if i_amount <= self.cash:
            self.coffee_inventory += i_amount
            self.cash -= i_amount
            return True
        else:
            return False
    
    def make_temp_distribution(self):
        # create series of numbers between TEMP_MIN and TEMP_MAX
        series = numpy.linspace(self.TEMP_MIN, self.TEMP_MAX, self.SERIES_DENSITY)
        
        # obtain mean and standard deviation from the series
        mean = numpy.mean(series)
        
        std_dev = numpy.std(series)
        
        #calculate probability density and return the list it creates
        return (numpy.pi * std_dev) * numpy.exp(-0.5 * ((series - mean) / std_dev) ** 2)
        # # This is nto a good bell curve, but it will do for now until more advance math
        # temps = []
        # # First, find the average between TEMP_MIN and TEMP_MAX
        # avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
        # # Find the distance between TEMP_MAX and the average
        # max_dist_from_avg = self.TEMP_MAX - avg
        
        # #Loop through all posssible temperatures
        # for i in range(self.TEMP_MIN, self.TEMP_MAX):
        #     # How far away is the temperature from the average
        #     # abs() gives the absolute value
        #     dist_from_avg = abs(avg - i)
        #     # How far away si the dist_from_avg from the maximum?
        #     # This will be lower for temps at the extremes
        #     dist_from_max_dist = max_dist_from_avg - dist_from_avg
        #     # If the value is zero, make it one
        #     if dist_from_max_dist == 0:
        #         dist_from_max_dist = 1
        #     # Append the output of x_of_y to temps
        #     for t in x_of_y(int(dist_from_max_dist), i):
        #         temps.append(t)
        # return temps
        
    def increment_day(self):
        self.day += 1
        
    def daily_stats(self, temperature):
        print("You have $" + str(self.cash) + " cash on hand and the temperature is " + str(temperature) + ".")
        print("You have enough coffee on hand to make " + str(self.coffee_inventory) + " cups\n")
        
    def day_header(self):
        print("\n-----| Day " + str(self.day) + " @ " + str(self.shop_name) + " |-----")
    
    def daily_sales(self, temperature, advertising, cup_price):
        
        # randomize advertising effectiveness
        adv_coefficient = random.randint(20, 80) / 100
        
        # higher priced coffee not selling as well
        price_coeficient = int((cup_price * (random.randint(50, 250) / 100)))
        
        # run the sales
        sales = int((self.TEMP_MAX - temperature) * (advertising * adv_coefficient))
        
        # if price to high, we don't sell anything
        if price_coeficient > sales:
            sales = 0
        else:
            sales -= price_coeficient
            
        if sales > self.coffee_inventory:
            sales = self.coffee_inventory
            print("You would have sold more coffee but you ran out. Be sure to buy additional inventory.")
        return sales
    
    @property
    def weather(self):
        # Generate a random temperature between 20 and 90
        return random.choice(self.temps)
    
        
    
