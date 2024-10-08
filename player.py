class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.max_health = 100
        self.health = 100
        self.max_energy = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory_name = []
        self.inventory_size = []
        self.inventory = []
        self.heals = []
        self.attacks = []
        self.speed = 1
        self.max_defense = 100
        self.defense = 0
        self.attack = 0
        self.damage = 0

    def calculate_inventory_size(self):
      return sum(self.inventory_size)

    def no_of_heals(self):
      return len(self.heals)

    def no_of_attacks(self):
      return len(self.attacks)

  
    def add_item(self, item_instance):
        import time
        if self.calculate_inventory_size() + item_instance.size <= self.inventory_max_weight:
            self.inventory_name.append(item_instance.name)
            self.inventory_size.append(item_instance.size)
            self.inventory.append(item_instance)
            time.sleep(0.5)
            print("""
""" + item_instance.name + " has been added to inventory")
            time.sleep(0.5)
            print("""
Your inventory size is now: """ + str(self.calculate_inventory_size()) + """
""")
            time.sleep(0.5)
            if item_instance.heal == 0:
              self.attacks.append(item_instance.name)
            else:
              self.heals.append(item_instance.name)
            self.check_inventory()
        else:
            time.sleep(0.5)
            print("Your inventory is full...")
            time.sleep(0.5)
            self.check_inventory()
            time.sleep(0.5)
            e = input("Would you like to remove an item? (Y/N)" """
""")
            while e.title() != "Y" and e.title() != "N":
              time.sleep(0.5)
              e = input("Would you like to remove an item? (Y/N)" """
""")
            if e.title() == "N":
              time.sleep(0.5)
              print("You will not equip item. No items lost")
            while e.title() == "Y" and self.calculate_inventory_size() + item_instance.size > self.inventory_max_weight:
              time.sleep(0.5)
              item_remove = input("Enter item to remove. (To cancel type N/A)")
              if item_remove != "N/A":
                i = 0
                j = len(self.inventory_name)
                F = False
                while F == False:
                  i = 0
                  while F == False and i < j:
                    if self.inventory_name[i] == item_remove:
                      F = True
                    else:
                      i = i + 1        
                  if F == False:
                    time.sleep(0.5)
                    item_remove = input("""
Enter item in your inventory to remove (to cancel type N/A)
""")            
                    if item_remove == "N/A":
                      F = True
              if item_remove != "N/A":
                self.remove_item(self.inventory[i])
                if self.calculate_inventory_size() + item_instance.size > self.inventory_max_weight:
                  time.sleep(0.5)
                  print("Your inventory size now is: " + str(self.calculate_inventory_size()))
                  time.sleep(0.5)
                  print("You need to remove more items""""
""")
                  time.sleep(0.5)
                  e = input("Would you like to remove an item? (Y/N)""""
""")
                  while e.title() != "Y" and e.title() != "N":
                    time.sleep(0.5)
                    e = input("Would you like to remove an item? (Y/N)" """
""")
                  if e.title() == "N":
                    time.sleep(0.5)
                    print("""
You did not equip the """ + item_instance.name + """
""")
                    time.sleep(0.5)
                    print("Your inventory size is: " + str(self.calculate_inventory_size()) + """
""")
                else:
                  time.sleep(0.5)
                  print("You have added your new item to your inventory" """
""")
                  self.inventory_name.append(item_instance.name)
                  self.inventory_size.append(item_instance.size)
                  self.inventory.append(item_instance)
                  if item_instance.heal == 0:
                    self.attacks.append(item_instance.name)
                  else:
                    self.heals.append(item_instance.name)
                  time.sleep(0.5)
                  print("""
""" + item_instance.name + " has been added to inventory" """
""")
                  time.sleep(0.5)
                  print("Your inventory size is now " + str(self.calculate_inventory_size()))
                  print("""
""")
                  e = "N"
              else:
                time.sleep(0.5)
                print("You have not removed an item, but cannot get the new one." """
""")
                time.sleep(0.5)
                print("Your inventory size is: " + str(self.calculate_inventory_size()))
                print("""
""")
                e = "N"
                
              

    def heal_item(self, item_instance):
        self.health += item_instance.heal
        item_instance.durability -= 1
        if self.health > self.max_health:
          self.health = self.max_health
        print("""
Your health increased by """ + str(item_instance.heal))
        print("""
Your health is now """ + str(self.health))

    def use_item(self,item_instance):
      self.damage = self.attack + item_instance.damage
      item_instance.durability -= 1
      self.energy -= item_instance.energy_taken
      print("Your attack took " + str(item_instance.energy_taken) + " energy")
      print("Your energy is now " + str(self.energy))


    def remove_item(self, item_instance):
      import time
      i = 0
      while i != len(self.inventory_name):
        if item_instance.name == self.inventory_name[i]:
          j = self.inventory_name[i]
          time.sleep(0.5)
          print("""
You are removing """ + j + """ from your inventory
""")
          self.inventory_name.remove(item_instance.name)
          break
        else:
          i = i + 1
      self.inventory_size.pop(i)
      self.inventory.pop(i)
      if item_instance.heal == 0:
        self.attacks.remove(j)
      else:
        self.heals.remove(j)
      print("""
""")
      self.check_inventory()
      

  
    def broken_item(self,item_instance):
      import time
      time.sleep(0.5)
      print("""
""")
      print('Your ' + str(item_instance.name) + ' broke. It will be removed from your inventory.')
      i = 0
      while i < len(self.inventory_name):
        if item_instance.name == self.inventory_name[i]:
          y = self.inventory_name[i]
          self.inventory_name.pop(i)
          break
        else:
          i = i + 1
      self.inventory_size.pop(i)
      self.inventory.pop(i)
      if item_instance.heal == 0:
        self.attacks.remove(y)
      else:
        self.heals.remove(y)
      time.sleep(0.5)
      print("""Full inventory:
""", self.inventory_name)
      time.sleep(0.5)
      print("""Full inventory sizes:
""", self.inventory_size)
      time.sleep(0.5)
      print("""Healing items:
""", self.heals)
      time.sleep(0.5)
      print("""Attack items:
""", self.attacks)
          

    def show_stats(self):
      import time
      time.sleep(0.5)
      print("Your health: " + str(self.health))
      time.sleep(0.5)
      print("Your energy: " + str(self.energy))
      time.sleep(0.5)
      print("Your speed: " + str(self.speed))
      time.sleep(0.5)
      print("Your defense: " + str(self.defense))
      time.sleep(0.5)
      print("Your attack: " + str(self.attack) + """
""")
      time.sleep(0.5)

        
    def check_inventory(self):
      import time
      time.sleep(0.5)
      print("""Item names:
""", self.inventory_name, """
""")
      time.sleep(0.5)
      print("""Item sizes:
""", self.inventory_size, """
""")
      time.sleep(0.5)
      print("""Your max inventory size is: 
""", self.inventory_max_weight, """
""")
    
    def want_item(self, place):
        import time
        i = 0
        if len(place.items) == 0:
          print("There are no items here")
        else:
          while i < len(place.items):
            time.sleep(0.5)
            print("""
There is a """ + place.items[i].name + " of size " + str(place.items[i].size) + " that has a damage of " + str(place.items[i].damage) + " and healing effect of " + str(place.items[i].heal) + ". It has a durabilty of " + str(place.items[i].durability) + " and takes " + str(place.items[i].energy_taken) + " energy to use.")
            time.sleep(0.75)
            ans = input("""
Would you like this item? (Y/N)""")
            if ans.title() == 'Y':
              self.add_item(place.items[i])
              place.remove_item(place.items[i])
              self.check_inventory()
            elif ans.title() == 'N':
              time.sleep(0.5)
              print("""
Item not added
""")
              i = i + 1
            else:
              time.sleep(0.5)
              print("""
Enter Y/N to answer
""")
              