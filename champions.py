from stats import*

class Fizz(Stats):
    def __init__(self,attack_damage, ability_power, health, mana, level, attack_range, damage_dealt, cooldown):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range, damage_dealt, cooldown)
    
    def basic_attack(self):
        self.damage_dealt = fizz_stat.attack_damage
        print(f"Fizz dealt {fizz_stat.attack_damage} Physical Damage")

    def use_q_ability(self):
        self.damage_dealt = int(120 + (fizz_stat.ability_power * 1.2 - fizz_stat.ability_power))
        self.cooldown = 5
        print(f"Fizz dealt {self.damage_dealt} Magical Damage, Going off for a 5 Seconds Cooldown")
    
fizz_stat = Fizz(90,0,800,600,1,125,0,0)
avaiable_champion = 1

class Brand(Stats):
    def __init__(self, attack_damage, ability_power, health, mana, level, attack_range, damage_dealt, cooldown):
        super().__init__(attack_damage, ability_power, health, mana, level, attack_range, damage_dealt, cooldown)

    def basic_attack(self):
        self.damage_dealt = brand_stat.attack_damage
        print(f"Brand dealt {brand_stat.attack_damage} Physical Damage")

    def use_q_ability(self):
        self.damage_dealt = int(200 + (brand_stat.ability_power * 1.3 - brand_stat.ability_power))
        self.cooldown = 15
        print(f"Brand dealt {self.damage_dealt} Magical Damage, Going off for a 15 Seconds Cooldown")

brand_stat = Brand(90,0,750,750,1,650,0,0)
avaiable_champion = 2