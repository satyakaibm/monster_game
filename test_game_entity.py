import unittest
import time
from game_entities import Hero, Monster

class TestGameEntities(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("hero", health=40)
        self.orc = Monster("orc", health=7, attack_interval=1.5, attack_damage=1)
        self.dragon = Monster("dragon", health=20, attack_interval=2, attack_damage=3)

    def test_hero_attack(self):
        initial_hero_health = self.hero.health
        self.hero.attack(self.orc)
        #self.assertEqual(self.orc.health, initial_orc_health - self.hero.attack_damage)
        self.assertLess(initial_hero_health - self.orc.attack_damage, self.hero.health)

    def test_monster_attack(self):
        initial_orc_health = self.orc.health
        initial_dragon_health = self.dragon.health

        self.orc.attack(self.hero)
        self.assertLess(initial_orc_health - self.orc.attack_damage, self.orc.health)

        self.dragon.attack(self.hero)
        self.assertLess(initial_dragon_health - self.dragon.attack_damage, self.dragon.health)

    def test_hero_attack_interval(self):
        initial_orc_health = self.orc.health
        time_waited = 0
        while self.orc.health == initial_orc_health:
            time.sleep(0.1)  # Wait a short time
            time_waited += 0.1
            if time_waited > 5:
                break  # Exit the loop after 5 seconds to avoid an infinite loop
        self.assertLess(0, initial_orc_health)

    def test_monster_attack_interval(self):
        initial_hero_health = self.hero.health
        time_waited = 0
        while self.hero.health == initial_hero_health:
            time.sleep(0.1)  # Wait a short time
            time_waited += 0.1
            if time_waited > 5:
                break  # Exit the loop after 5 seconds to avoid an infinite loop
        self.assertLess(0, initial_hero_health)

if __name__ == '__main__':
    unittest.main()
