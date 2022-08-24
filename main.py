from stats import*
from champions import*
import time

if __name__ == "__main__":
    stat = Stats(50,0,550,400,1,125,0,0)
    print("List of Champions:")
    print("Brand")
    print("Fizz")
    action = input("Please select your champion: ")
    if action == "Brand":
        print("Basic Attack")
        print("Use Q Ability")
        action = input("It's your turn now, please choose an action: ")
        if action == "Basic Attack":
            brand_stat.basic_attack()
            cooldown = 0
        elif action == "Use Q Ability":
            brand_stat.use_q_ability()
            cooldown = brand_stat.cooldown
    elif action == "Fizz":
        print("Basic Attack")
        print("Use Q Ability")
        action = input("It's your turn now, please choose an action: ")
        if action == "Basic Attack":
            fizz_stat.basic_attack()
            cooldown = 0
        elif action == "Use Q Ability":
            fizz_stat.use_q_ability()
            cooldown = fizz_stat.cooldown
    if cooldown > 0:
        for i in range(cooldown):
            cooldown -= 1
            time.sleep(1)
            print(cooldown)
            if cooldown == 0:
                print("Q is now ready to use")