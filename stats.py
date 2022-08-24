class Stats:
    def __init__(self,attack_damage, ability_power, health, mana, level, attack_range):
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.health = health
        self.mana = mana
        self.level = level
        self.attack_range = attack_range
    
    def levelup(self):
        self.attack_damage += 5
        self.ability_power += 5
        self.health += 5
        self.mana += 5
        self.level += 1

    def use_q_ability(self):
        pass

    def use_w_ability(self):
        pass

    def use_e_ability(self):
        pass

    def use_r_ability(self):
        pass
    
    def displaystat(self):
        pass
