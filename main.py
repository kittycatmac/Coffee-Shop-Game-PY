import pickle
import re
from pathlib import Path

from coffee_shop_simulator import CoffeeShopSimulator

# If save file exists, see if the player want to load it
run_game = True
if Path(CoffeeShopSimulator.SAVE_FILE).is_file():
    # save game exists, do they want to load it?
    response = CoffeeShopSimulator.prompt("There's saved game. Do you want to load it? (Y/N)", True)
    if re.search("y", response, re.IGNORECASE):
        # Load game and run
        with open(CoffeeShopSimulator.SAVE_FILE, mode="rb") as f:
            game = pickle.load(f)
            game.run()
            run_game = False
    else:
        print("HINT: If you don't want to see this prompt again remove the " + CoffeeShopSimulator.SAVE_FILE + " file.\n")

if run_game:
    # creates the game object and runs it
    game = CoffeeShopSimulator()
    game.run()
    
print("\nThanks for playing. Have a great rest of your day!\n")