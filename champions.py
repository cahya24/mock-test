from stats import*

class Fizz(Stats):
    def __init__(self,attack_damage, ability_power, health, mana, level, attack_range, damage_dealt):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range, damage_dealt)
    
    def basic_attack(self):
        self.damage_dealt = fizz_stat.attack_damage
        print(f"Fizz dealt {fizz_stat.attack_damage} damage")

    def use_q_ability(self):
        self.damage_dealt = 120 + (fizz_stat.ability_power * 1.2 - fizz_stat.ability_power)
        print(f"Fizz dealt 120 + 20% of {fizz_stat.ability_power} Ability Power, Cooldown for 5 seconds")
    
fizz_stat = Fizz(90,0,800,600,1,125,0)

class Brand(Stats):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range, damage_dealt):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range, damage_dealt)

    def basic_attack(self):
        self.damage_dealt = brand_stat.attack_damage
        print(f"Brand dealt {brand_stat.attack_damage} damage")

    def use_q_ability(self):
        self.damage_dealt = 200 + (brand_stat.ability_power * 1.3 - brand_stat.ability_power)
        print(f"Brand dealt 200 + 30% of {brand_stat.ability_power} Ability Power, Cooldown for 15 seconds")

brand_stat = Brand(90,0,750,750,1,650,0)