# Simple Pokemon game
# Player chooses a Pokeball selection and is then given a random Pokemon for their 'starter' Pokemon 
# Pokemon is selected depending on colour chosen. 
print("Hello! Welcome to the world of Pokemon! Are you ready to start your adventure?")
# Ask for the players name
player_name = input("What is your name?")
print("Nice to meet you,", player_name + "!")
print("Are you ready to start your adventure?!")
# Ask the player to choose a Pokeball. Pokeballs correspond to the colour/type of the Pokemon 
print("Choose your Pokeball and reveal your starter Pokemon!")
print("Red Pokeball? Blue Pokeball? Green Pokeball? Mystery Pokeball")
chosen_pokeball = input("Which Pokeball do you choose?").lower() 
if chosen_pokeball == "red":
    print("You chose the Red Pokeball!")
    print("Inside... it's Charmander! The fire-type Pokemon!")
elif chosen_pokeball == "blue":
    print("You chose the Blue Pokeball!")
    print("Inside... it's Squirtle! The water-type Pokemon!")
elif chosen_pokeball == "green":
    print("You chose the Green Pokeball! ")
    print("Inside... it's Bulbasaur! The grass-type Pokemon!")
elif chosen_pokeball == "mystery":
    print("You chose the mystery Pokeball! Let's see... it's Pikachu! The electric-type Pokemon!")
else:
    print("Hmm... that's not a Pokeball I recognise! Please restart and try again.")

# Farewell message to the player

print("Best of luck on your Pokémon journey, " + player_name + "! Catch 'em all!")
