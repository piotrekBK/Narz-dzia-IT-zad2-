def attack(attacker, defender):
    damage = attacker["attack"]
    defender["hp"] -= damage
    print(attacker["name"], "hits", defender["name"], "for", damage)