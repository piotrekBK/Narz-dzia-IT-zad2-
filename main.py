from combat import attack
from characters import player, enemy

def main():
    while player["hp"] > 0 and enemy["hp"] > 0:
        attack(player, enemy)
        attack(enemy, player)

    if player["hp"] <= 0:
        print("You lost!")
    else:
        print("You won!")

if __name__ == "__main__":
    main()