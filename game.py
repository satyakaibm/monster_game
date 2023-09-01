from game_entities import hero, orc, dragon

print("Welcome to the Monster Slayer game!")
print("Type 'attack orc' or 'attack dragon' to fight.")

while hero.alive and (orc.alive or dragon.alive):
    command = input("Type: ").lower()
    if command == "attack orc" and orc.alive:
        hero.attack(orc)
    elif command == "attack dragon" and dragon.alive:
        hero.attack(dragon)
    else:
        print("Invalid target or target is already defeated.")

if orc.alive or dragon.alive:
    print("You lose! Monsters win.")
else:
    print("Congratulations! You have defeated all the monsters!")
