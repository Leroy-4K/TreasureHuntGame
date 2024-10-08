class Battle:
  def __init__(self, player, enemy):
    self.player = player
    self.enemy = enemy

  def battle(self, player, enemy):
    you_win = False
    import time
    import random
    player.show_stats()
    print("""
""")
    time.sleep(2)
    enemy.show_stats()
    Battle_over = False
    total_speed = player.speed + enemy.speed
    turn = 1
    while Battle_over == False:
        print("""
Turn """ + str(turn))
        time.sleep(2)
        first_attack = int((player.speed/total_speed)*100)
        if random.randint(0,100) <= first_attack:
          print("""
You faster than your opponent this turn
You move first
""")
          time.sleep(2)
          action = input("""
Enter 'H' to heal
Enter 'A' to attack
Enter 'R' to rest
""")
          while action.title() != 'H' and action.title() != 'A' and action.title() != 'R':
              action = input("""
Enter 'H' to heal
Enter 'A' to attack
Enter 'R' to rest""")
          if action.title() == 'R':
            print("You rested")
            print("You gained 50 rest energy")
            player.energy += 50
            if player.energy > player.max_energy:
              player.energy = player.max_energy
            print("Your energy is " + str(player.energy))
          if action.title() == 'H':
            print(player.heals)
            time.sleep(0.5)
            healing_item = input("""
Which healing item would you like to use
""")
            time.sleep(0.5)
            if player.no_of_heals() == 0:
              healing_item = "N/A"
            if healing_item == "N/A":
              time.sleep(0.5)
              print("""
You attempt to heal with nothing.
Surprisingly this does not work.
""")
            else:
              i = 0
              j = len(player.inventory_name)
              Found = False
              while Found == False:
                i = 0
                while Found == False and i < j:
                  if player.inventory_name[i] == healing_item:
                    Found = True
                  else:
                    i = i + 1
                if Found == True:
                  if player.inventory[i].heal == 0:
                    Found = False
                if Found == False:
                  time.sleep(0.5)
                  healing_item = input("""
  Enter a healing item in your inventory""")
                  if healing_item == "N/A":
                    Found = True
                    time.sleep(0.5)
                    print("""
You attempt to heal with nothing.
Surprisingly this does not work.
""")
            
            
            if healing_item != "N/A":
              time.sleep(0.5)
              player.heal_item(player.inventory[i])
              
              if player.health > player.max_health:
                player.health = player.max_health
                
              if player.inventory[i].durability <= 0:
                time.sleep(0.5)
                player.broken_item(player.inventory[i])
              
          if action.title() == 'A':
            print(player.attacks)
            time.sleep(0.5)
            attack_item = input("""
Which attack item would you like to use?
Enter N/A (in caps) to not use a weapon
No attack weapon is automatic N/A
""")
            if player.no_of_attacks() == 0:
              attack_item = "N/A"
            if attack_item == "N/A":
              time.sleep(0.5)
              print("You attack with no weapon")
              player.damage = player.attack
            else:
              i = 0
              j = len(player.inventory_name)
              Found = False
              while Found == False:
                i = 0
                while Found == False and i < j:
                  if player.inventory_name[i] == attack_item:
                    Found = True
                  else:
                    i = i + 1
                if Found == True:
                  if player.inventory[i].damage == 0:
                    Found = False
                    time.sleep(0.5)
                    print("""
Must be attack item
""")
                  if player.energy - player.inventory[i].energy_taken < 0:
                    Found = False
                    time.sleep(0.5)
                    print("You do not have the energy to use this item")
                if Found == False:
                  time.sleep(0.5)
                  attack_item = input("""
Enter an attack item in your inventory
  """)
                  if attack_item == "N/A":
                    Found = True
                    time.sleep(0.5)
                    print("You attack with no weapon")
                    player.damage = player.attack
              if attack_item != "N/A":
                player.use_item(player.inventory[i])
                if player.inventory[i].durability <= 0:
                  player.broken_item(player.inventory[i])
                        
            if enemy.defense > 0:
              player.damage = int(player.damage - (player.damage * (enemy.defense/200)))
            enemy.health -= player.damage
            if enemy.health < 0:
              enemy.health = 0
            time.sleep(0.5)
            print("You did " + str(player.damage) + " damage")
            time.sleep(0.5)
            print("Enemy's health is " + str(enemy.health))
            
          if enemy.health <= 0:
            enemy.defeated = True
            Battle_over = True
          
          else:
            time.sleep(0.5)
            print("""
""")
            print("Enemy's turn")
            u = [enemy.special_move, enemy.normal_move_1, enemy.normal_move_2]
            h = random.choice(u)
            enemy.damage = int(enemy.attack - (enemy.attack * (player.defense/200)))
            if h == enemy.special_move and enemy.energy - 20 >= 0:
              enemy.damage += 30
              enemy.energy -= 20
              player.health -= enemy.damage
              if player.health < 0:
                player.health = 0
              time.sleep(0.5)
              print("Enemy uses " + str(h))
              time.sleep(0.5)
              print("Enemy attacks for " + str(enemy.damage) + " damage")
              time.sleep(0.5)
              print("Enemy has " + str(enemy.energy) + " energy left")
              time.sleep(0.5)
              print("You have " + str(player.health) + " health left")
              #add more enemy stuff#
              if player.health <= 0:
                Battle_over = True
            elif h == enemy.special_move and enemy.energy - 20 < 0:
              time.sleep(0.5)
              enemy.rest()
                
            elif h == enemy.normal_move_1 or h == enemy.normal_move_2:
              if enemy.energy - 10 >= 0:
                enemy.energy -= 10
                player.health -= enemy.damage
                if player.health < 0:
                  player.health = 0
                time.sleep(0.5)
                print("Enemy uses " + str(h))
                time.sleep(0.5)
                print("Enemy attacks for " + str(enemy.damage) + " damage")
                time.sleep(0.5)
                print("Enemy has " + str(enemy.energy) + " energy left")
                time.sleep(0.5)
                print("You have " + str(player.health) + " health left")
              else:
                time.sleep(0.5)
                enemy.rest()
   
            if player.health <= 0:
              Battle_over = True
        
        
        else:
          u = [enemy.special_move, enemy.normal_move_1, enemy.normal_move_2]
          h = random.choice(u)
          enemy.damage = int(enemy.attack - (enemy.attack * (player.defense/200)))
          time.sleep(0.5)
          print("""
You slower than your opponent this turn
You move second
""")
          if h == enemy.special_move and enemy.energy - 20 >= 0:
              enemy.damage += 30
              enemy.energy -= 20
              player.health -= enemy.damage
              if player.health < 0:
                player.health = 0
              time.sleep(0.5)
              print("Enemy uses " + str(h))
              time.sleep(0.5)
              print("Enemy attacks for " + str(enemy.damage) + " damage")
              time.sleep(0.5)
              print("Enemy has " + str(enemy.energy) + " energy left")
              time.sleep(0.5)
              print("You have " + str(player.health) + " health left")
              #add more enemy stuff#
              if player.health <= 0:
                Battle_over = True
                print("You died :(. Your family is heartbroken")
                exit()
          elif h == enemy.special_move and enemy.energy - 20 < 0:
            enemy.rest()

          elif h == enemy.normal_move_1 or h == enemy.normal_move_2:
            if enemy.energy - 10 >= 0:
              enemy.energy -= 10
              player.health -= enemy.damage
              if player.health < 0:
                player.health = 0
              time.sleep(0.5)
              print("Enemy uses " + str(h))
              time.sleep(0.5)
              print("Enemy attacks for " + str(enemy.damage) + " damage")
              time.sleep(0.5)
              print("Enemy has " + str(enemy.energy) + " energy left")
              time.sleep(0.5)
              print("You have " + str(player.health) + " health left")
            else:
              time.sleep(0.5)
              enemy.rest()          

          if player.health <= 0:
              Battle_over = True
              print("You died :(. Your family is heartbroken.")
              exit()
          
          action = input("""
Enter 'H' to heal
Enter 'A' to attack
Enter 'R' to rest
""")
          while action.title() != 'H' and action.title() != 'A' and action.title() != 'R':
              action = input("""
Enter 'H' to heal
Enter 'A' to attack
Enter 'R' to rest
""")
          if action.title() == 'R':
            print("You rested")
            print("You gained 50 rest energy")
            player.energy += 50
            if player.energy > player.max_energy:
              player.energy = player.max_energy
            print("Your energy is " + str(player.energy))
          if action.title() == 'H':
            print(player.heals)
            time.sleep(0.5)
            healing_item = input("""
Which healing item would you like to use
No healing items is automatic N/A
""")
            if player.no_of_heals() == 0:
              healing_item = "N/A"
            if healing_item == "N/A":
              time.sleep(0.5)
              print("""
You attempt to heal with nothing.
Surprisingly this does not work.
""")
            else:            
              i = 0
              j = len(player.inventory_name)
              Found = False
              while Found == False:
                i = 0
                while Found == False and i < j:
                  if player.inventory_name[i] == healing_item:
                    Found = True
                  else:
                    i = i + 1
                if Found == True:
                  if player.inventory[i].heal == 0:
                    Found = False
                if Found == False:
                  time.sleep(0.5)
                  healing_item = input("""
  Enter a healing item in your inventory
  """)
                  if healing_item == "N/A":
                    time.sleep(0.5)
                    print("""
You attempt to heal with nothing.
Surprisingly this does not work.
""")
                    Found = True
            if healing_item != "N/A":
              time.sleep(0.5)
              player.heal_item(player.inventory[i])
              if player.health > player.max_health:
                player.health = player.max_health
              if player.inventory[i].durability <= 0:
                player.broken_item(player.inventory[i])
            



            
          if action.title() == 'A':
            print(player.attacks)
            time.sleep(0.5)
            attack_item = input("""
Which attack item would you like to use
""")
            if player.no_of_attacks() == 0:
              attack_item = "N/A"
            if attack_item == "N/A":
              time.sleep(0.5)
              print("You attack with no weapon")
              player.damage = player.attack
            else:            
              i = 0
              j = len(player.inventory_name)
              Found = False
              while Found == False:
                i = 0
                while Found == False and i < j:
                  if player.inventory_name[i] == attack_item:
                    Found = True
                  else:
                    i = i + 1
                if Found == True:
                  if player.inventory[i].damage == 0:
                    Found = False
                  if player.energy - player.inventory[i].energy_taken < 0:
                    Found = False
                    time.sleep(0.5)
                    print("You do not have the energy to use this item")          
                if Found == False:
                  time.sleep(0.5)
                  attack_item = input("""
Enter an attack item in your inventory
  """)
                  if attack_item == "N/A":
                    Found = True
                    time.sleep(0.5)
                    print("You attack with no weapon")
                    player.damage = player.attack
              if attack_item != "N/A":
                time.sleep(0.5)
                player.use_item(player.inventory[i])
                if player.inventory[i].durability <= 0:
                  player.broken_item(player.inventory[i])              
              
            if enemy.defense > 0:
              player.damage = int(player.damage - (player.damage * (enemy.defense/200)))
            enemy.health -= player.damage
            if enemy.health < 0:
              enemy.health = 0
            time.sleep(0.5)
            print("You did " + str(player.damage) + " damage")
            time.sleep(0.5)
            print("Enemy's health is " + str(enemy.health))
          
      
        if enemy.health <= 0:
          enemy.defeated = True
          Battle_over = True
        if player.health <= 0:
          Battle_over = True
        if Battle_over == True:
          if enemy.health <= 0:
            print("You win")
            you_win = True
          else:
            print("You died. You family is heartbroken")
        turn = turn + 1
    if you_win == False:
      exit()
    else:
      player.inventory_max_weight += 10
      player.attack += 10
      player.defense += 10
      if player.defense > player.max_defense:
        player.defense = player.max_defense
      player.speed += 10
      player.max_health += 10
      player.health = player.max_health
      player.max_energy += 10
      player.energy = player.max_energy
      print("""
Your inventory size has increased by 10
All of your stats has been increased by 10
""")
      player.show_stats()