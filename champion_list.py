from champion import*

class Fizz(Champion):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range, cooldown):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range)
        self.cooldown = cooldown
    
    def basic_attack(self, target):
        damage = champ_fizz.attack_damage
        target.health -= damage
        print(f"Fizz dealt {damage} damage to Brand")

    def use_q_ability(self, target):
        damage = int(120 + (champ_fizz.ability_power * 1.2))
        target.health -= damage
        self.cooldown = 5
        print(f"Fizz dealt {damage} damage to Brand, Cooldown for 5 seconds")

champ_fizz = Fizz(60,0,800,400,1,125,0)

class Brand(Champion):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range, cooldown):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range)
        self.cooldown = cooldown

    def basic_attack(self, target):
        damage = champ_brand.attack_damage
        target.health -= damage
        print(f"Brand dealt {damage} damage to Fizz")
    
    def use_q_ability(self, target):
        damage = int(200 + (champ_brand.ability_power * 1.1))
        target.health -= damage
        self.cooldown = 8
        print(f"Brand dealt {damage} damage to Fizz, Cooldown for 8 seconds")

champ_brand = Brand(70,0,750,350,1,600,0)