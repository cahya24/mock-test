from champion import*

class Fizz(Champion):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range)

    def use_q_ability(self, target):
        target.health -= int(120 + (champ_fizz.ability_power * 1.2))

champ_fizz = Fizz(60,0,800,400,1,125)

class Brand(Champion):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range)

champ_brand = Brand(70,0,750,350,1,600)