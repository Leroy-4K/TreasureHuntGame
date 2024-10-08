class Train():
  def __init__(self):
    self = self
  def train(self, player):
      import time
      print("You decide to train")
      time.sleep(0.5)
      print("What would you like to train: """"
""")
      time.sleep(0.5)
      print("""1. Energy
""")
      time.sleep(0.5)
      print ("2. Health""""
""")
      time.sleep(0.5)
      print("3. Defense""""
""")
      time.sleep(0.5)
      print("4. Base Attack""""
""")
      t = input("5. Speed" """
""")
      win = False
      b = 3
      
      while t != "1" and t != "2" and t != "3" and t != "4" and t != "5":
        time.sleep(0.5)
        print("What would you like to train: """"
""")
        time.sleep(0.5)
        print("""1. Energy
""")
        time.sleep(0.5)
        print ("2. Health""""
""")
        time.sleep(0.5)
        print("3. Defense""""
""")
        time.sleep(0.5)
        print("4. Base Attack""""
""")
        time.sleep(0.5)
        t = input("5. Speed""""
""")
        
      while b > 0 and win == False:
        time.sleep(0.5)
        print("To train you must type the following letters as fast as you can" """
""")
        i=0
        l=''
        import time
        import random
        time.sleep(0.5)
        a = 'abcdefghijklmnopqrstuvwxyz'
        word = random.sample(a,5)
        while i != 5:
          l = l + str(word[i])
          i = i + 1
        print(l + """
""")
        start = time.time()
        g = input("Type these letters in order")
        while g.lower() != l:
          g = input("Type these letters in order")
        end = time.time()
        s = end-start
        if s < 4:
          print('You took', s,'seconds and won!'"""
""")
          win = True
        else:
          print('You took', s,'seconds and lost! Try again' """
""")
          b -= 1
      if win == True:
        if t == "1":
          if b == 3:
            print("Your max energy went up by 15""""
  """)
            player.max_energy += 15
          elif b == 2:
            print("Your max energy went up by 10""""
  """)
            player.max_energy += 10
          elif b == 1:
            print("Your max energy went up by 5""""
  """)
            player.max_energy += 5
          else:
            print("Your max energy did not increase")
          player.energy = player.max_energy
        if t == "2":
          if b == 3:
            print("Your max health went up by 15""""
  """)
            player.max_health += 15
          elif b == 2:
            print("Your max health went up by 10""""
  """)
            player.max_health += 10
          elif b == 1:
            print("Your max health went up by 5""""
  """)
            player.max_health += 5
          else:
            print("Your max health did not increase")
          player.health = player.max_health
        
        if t == "3":
          if b == 3:
            print("Your defense went up by 15""""
  """)
            player.defense += 15
            if player.defense > player.max_defense:
              player.defense = player.max_defense
          elif b == 2:
            print("Your defense went up by 10""""
  """)
            player.defense += 10
            if player.defense > player.max_defense:
              player.defense = player.max_defense
          elif b == 1:
            print("Your defense went up by 5""""
  """)
            player.defense += 5
            if player.defense > player.max_defense:
              player.defense = player.max_defense
          else:
            print("Your defense did not increase")
        
        if t == "4":
          if b == 3:
            print("Your attack went up by 15""""
  """)
            player.attack += 15
          elif b == 2:
            print("Your attack went up by 10""""
  """)
            player.attack += 10
          elif b == 1:
            print("Your attack went up by 5""""
  """)
            player.attack += 5
          else:
            print("Your attack did not increase")
        
        elif t == "5":
          if b == 3:
            print("Your speed went up by 15""""
  """)
            player.speed += 15
          elif b == 2:
            print("Your speed went up by 10""""
  """)
            player.speed += 10
          elif b == 1:
            print("Your speed went up by 5""""
  """)
            player.speed += 5
          else:
            print("Your speed did not increase""""
""")
      player.show_stats()