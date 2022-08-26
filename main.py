from champion import*
from champion_list import*
import time

if __name__ == "__main__":
    champ_fizz.displaystat()
    champ_fizz.levelup()
    champ_fizz.displaystat()
    print("List of Champions:")
    print("Brand")
    print("Fizz")
    action = input("Please select your champion: ")
    if action == "Brand":
        print("-" * 99)
        print("Basic Attack")
        print("Use Q Ability")
        action = input("It's your turn now, please choose an action: ")
        if action == "Basic Attack":
            print("-" * 99)
            champ_brand.basic_attack(champ_fizz)
            cooldown = 0
        elif action == "Use Q Ability":
            print("-" * 99)
            champ_brand.use_q_ability(champ_fizz)
            cooldown = champ_brand.cooldown
    elif action == "Fizz":
        print("-" * 99)
        print("Basic Attack")
        print("Use Q Ability")
        action = input("It's your turn now, please choose an action: ")
        if action == "Basic Attack":
            print("-" * 99)
            champ_fizz.basic_attack(champ_brand)
            cooldown = 0
        elif action == "Use Q Ability":
            print("-" * 99)
            champ_fizz.use_q_ability(champ_brand)
            cooldown = champ_fizz.cooldown
    if cooldown > 0:
        for i in range(cooldown):
            cooldown -= 1
            time.sleep(1)
            print(cooldown)
            if cooldown == 0:
                print("Q is now ready to use")
    champ_brand.displaystat()
    champ_fizz.displaystat()