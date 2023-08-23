# monster_game
attack monsters until its alive from command line instructions 

# Requirement
1. The player controls a hero who fights two monsters: an orc and a dragon.
2. The hero has 40 health points, the orc has 7, the dragon has 10.
3. Every 1500ms (1.5sec) the orc attacks the hero for 1 damage, which means that the hero loses 1 health point.
4. Every 2000ms (2sec), the dragon attacks the hero for 3 damages, which means that the hero loses 3 health points.
5. Each time the player types "orc" or "dragon", the hero attacks the corresponding monster for 2 damage.
6. If the orc's or dragon's health points are reduced to zero, it is dead and can neither attack nor be attacked.
7. If both monsters die, the player wins the game.
8. If the hero's health points are reduced to zero, the player loses the game.
9. Display text messages on the console to keep the player informed when something happens, 
e.g. "Hero hits orc. Orc health is 5". 

Note: Don't include a GUI.

# Action Item:
Here's the implementation with separate classes for each action and organized in different modules:

First, I have created a module named "game_entities.py"
In this module, I've defined the Character, Monster, and Hero classes along with their methods. 
In the same directory, I can created another Python file to run the game using these entities.

Second module named "game.py"

# To run the code, follow these steps:

1. Open a Git Bash terminal or command prompt.
2. Checkout the code from git repo
   git clone https://github.com/satyakaibm/monster_game.git
   
3. Navigate to the directory
4. Ensure python is installed locally in your laptop or machine
5. Run the game by executing the following command:
   
   python game.py

6.Follow the instructions to interact with the game using the commands 
"orc" or "dragon".

