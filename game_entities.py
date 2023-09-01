import threading
import time

class Character:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.alive = True
        self.lock = threading.Lock()

    def attack(self, target):
        target.receive_damage(self.name, self.attack_damage)

    def receive_damage(self, attacker_name, damage):
        with self.lock:
            self.health = max(self.health - damage, 0)
            print(f"{attacker_name.capitalize()} hits {self.name}. {self.name.capitalize()} health is {self.health}")
            if self.health == 0:
                self.alive = False
                print(f"{self.name.capitalize()} is defeated!")

class Monster(Character):
    def __init__(self, name, health, attack_interval, attack_damage):
        super().__init__(name, health, attack_damage)
        self.attack_interval = attack_interval
        self.thread = threading.Thread(target=self.attack_loop)
        self.thread.daemon = True
        self.thread.start()

    def attack_loop(self):
        while self.alive:
            time.sleep(self.attack_interval)
            if self.alive:
                if hero.alive:
                    self.attack(hero)

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health, attack_damage=2)

hero = Hero("hero", health=40)
orc = Monster("orc", health=7, attack_interval=1.5, attack_damage=1)
dragon = Monster("dragon", health=20, attack_interval=2, attack_damage=3)
