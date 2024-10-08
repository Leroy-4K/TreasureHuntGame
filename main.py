from place import Place
from player import Player
from item import Item
from char import Char
from battle import Battle
from train import Train
from map import Map

class Game():
    def __init__(self):
      self.current_place = None
    def setup(self):
        #The map
        self.map = Map()
        #Char w/ stats and moves
        self.brother = Char("Brother", 100, 0.5, 10, 50, 0, 'Headbutt', 'Punch', 'Kick')
        self.Timmy = Char("Timmy", 500, 80, 200, 500, 100, 'Timmy Nuclear Blast', 'Timmy Blast', 'Timmy Punch')
        self.MysteryMan = Char("Mystery Man", 150, 3, 30, 100, 15, 'Silent Destruction', 'Shadow Bind', 'Stab')
        self.Dragon = Char("Dragon", 500, 10, 150, 100, 150, "Dragon Blast", "Dragon Breath", "Dragon Roar")
        self.Fly = Char("Fly", 10, 1000, 5, 10000, 125, "Bzzt", "Bzzt", "Bzzt")
        self.TreasureHunter = Char("Treasure Hunter", 200, 45, 45, 100, 40, "Gun Shot", "Slap", "Elbow Drop")
        self.RegularGuy = Char("Regular Guy", 100,1,7,100,10,"Bulldoze", "Push", "Shove")
        self.CastleProtector = Char("Castle Protector", 300, 80, 10, 300, 60, 'Spear attack', 'Sword attack', 'Dagger attack')
        self.CastleDefender = Char("Castle Defender", 400, 125, 20, 100, 75, "Piledriver", "German Suplex", "Spinebuster")
        self.Thief = Char("Thief", 200, 150, 30, 60, 20, "Stealth Attack", "Sneak Attack", "Silent Attack")
      
        # places
        self.home = Place('Home', self.brother)
        self.warlington = Place('Warlington', self.MysteryMan)
        self.castle = Place('Castle', self.Dragon)
        self.white_bridge = Place('White Bridge', self.Timmy)
        self.steampond = Place("Steampond", self.TreasureHunter)
        self.mistport = Place("Mistport", self.RegularGuy)
        self.dawnmount = Place("Dawnmount", self.CastleProtector)
        self.falsepeak = Place('Falsepeak', self.Fly)
        self.claykeep = Place("Claykeep", self.Thief)
        self.magewood = Place("Magewood", self.CastleDefender)
        
        #Places that are next to each other
        
        self.home.add_next_place(self.warlington)
        self.home.add_next_place(self.white_bridge)
        self.warlington.add_next_place(self.falsepeak)
        self.white_bridge.add_next_place(self.falsepeak)
        self.white_bridge.add_next_place(self.steampond)
        self.steampond.add_next_place(self.mistport)
        self.steampond.add_next_place(self.claykeep)
        self.steampond.add_next_place(self.white_bridge)
        self.mistport.add_next_place(self.dawnmount)
        self.mistport.add_next_place(self.magewood)
        self.mistport.add_next_place(self.steampond)
        self.dawnmount.add_next_place(self.mistport)
        self.dawnmount.add_next_place(self.castle)
        self.falsepeak.add_next_place(self.warlington)
        self.falsepeak.add_next_place(self.white_bridge)
        self.falsepeak.add_next_place(self.claykeep)
        self.claykeep.add_next_place(self.falsepeak)
        self.claykeep.add_next_place(self.steampond)
        self.claykeep.add_next_place(self.magewood)
        self.magewood.add_next_place(self.claykeep)
        self.magewood.add_next_place(self.mistport)
        self.magewood.add_next_place(self.castle)
      
        # healing items
      
        self.medicine = Item('Medicine', 0, 10, 1, 1, 0)
        self.medicine1 = Item('Medicine', 0, 10, 1, 1, 0)
        self.bandages = Item('Bandages', 0, 5, 1, 1, 0)
        self.healing_potion = Item('Healing Potion', 0, 30, 3, 1,0)
        self.healing_potion1 = Item('Healing Potion', 0, 30, 3, 1,0)
        self.med_kit = Item("Med Kit", 0, 50, 5, 1, 0)
        self.med_kit1 = Item("Med Kit", 0, 50, 5, 1, 0)
        self.healing_vial = Item("Healing Vial", 0, 75, 7, 1, 0)
        self.healing_vial1 = Item("Healing Vial", 0, 75, 7, 1, 0)
        self.healing_vial2 = Item("Healing Vial", 0, 75, 7, 1, 0)
        self.dragon_tears = Item("Dragon Tears", 0, 500, 30, 1, 0)
        self.dragon_tears1 = Item("Dragon Tears", 0, 500, 30, 1, 0)
        # attacking items
        
        self.hammer = Item('Hammer', 20, 0, 10, 20, 5)
        self.pen = Item('Pen', 2, 0, 1, 5, 1)
        self.pen1 = Item('Pen', 2, 0, 1, 5, 1)
        self.sword = Item('Sword', 30, 0, 10, 7, 10)
        self.sword1 = Item('Sword', 30, 0, 10, 7, 10)
        self.one_shot = Item('One Shot', 10000, 0, 10, 1, 110)
        self.mythical_sword = Item("Mythical Sword", 75, 0, 25, 25, 30)
        self.dagger = Item("Dagger", 15, 0, 3, 10, 3)
        self.pan = Item("Frying Pan", 5, 0, 5, 100, 1)
        self.rock = Item("Rock", 7, 0, 1, 7, 1)
        self.spear = Item("Spear", 25, 0, 10, 15, 15)
        self.screwdriver = Item("Screwdriver", 2, 0, 1, 2, 1)
        self.throngler = Item("Throngler", 100, 0, 35, 25, 45)
        self.dragon_tooth_spear = Item("Dragon Tooth Spear", 90, 0, 15, 50, 35)
        self.dragon_deity_claws = Item("Dragon Deity Claws", 95, 0, 10, 5, 10)
        self.dragon_deity_claws1 = Item("Dragon Deity Claws", 95, 0, 10, 5, 10)

        #game mechanics?
        
        self.train = Train()
        self.battle = Battle('player', 'enemy')

        #items in places
        self.home.add_item(self.pan)
        self.home.add_item(self.screwdriver)
        self.home.add_item(self.pen)
        
        self.warlington.add_item(self.dagger)
        self.warlington.add_item(self.med_kit)
        self.warlington.add_item(self.hammer)

        self.white_bridge.add_item(self.med_kit)
        self.white_bridge.add_item(self.healing_vial)
        self.white_bridge.add_item(self.dragon_tears)

        self.steampond.add_item(self.mythical_sword)
        self.steampond.add_item(self.med_kit1)
        self.steampond.add_item(self.healing_potion)

        self.mistport.add_item(self.bandages)
        self.mistport.add_item(self.throngler)
        self.mistport.add_item(self.healing_vial1)

        self.dawnmount.add_item(self.medicine1)
        self.dawnmount.add_item(self.sword)
        self.dawnmount.add_item(self.dragon_deity_claws)

        self.falsepeak.add_item(self.rock)
        self.falsepeak.add_item(self.sword1)
        self.falsepeak.add_item(self.spear)

        self.claykeep.add_item(self.healing_vial2)
        self.claykeep.add_item(self.healing_potion1)
        self.claykeep.add_item(self.pen1)

        self.magewood.add_item(self.dragon_tooth_spear)
        self.magewood.add_item(self.dragon_deity_claws1)
        self.magewood.add_item(self.dragon_tears1)

        # home will be the starting place
        self.current_place = self.home
      
    def move_place(self):
      if self.current_place.name != "Castle":
        self.map.show_map()
        d = False
        while d == False:
          self.current_place.show_next_places()
          next_place = input("""
Enter next place
""")      
          if next_place in self.current_place.next_places_name:
            i = 0
            while next_place != self.current_place.next_places[i].name:
              i = i + 1
            d = True
        self.current_place = self.current_place.next_places[i]
        print("Current place:" + str(self.current_place.name))
      else:
        print("You cannot move from the Castle")
      

    
    def enter_place(self, player):
      import time
      if self.current_place.enter == False:
        self.current_place.enter = True
        
        self.train.train(player)
        self.current_place.enemy.see()
        opt = input("""
1. Approach to talk
2. Approach to fight
3. Search for items
""")
        while opt != "1" and opt != "2" and opt != "3":
          opt = input("""
1. Approach to talk
2. Approach to fight
3. Search for items
""")   
        if opt == "1":
          self.current_place.enemy.chat()
          self.current_place.enemy.talk = True
          opt = ''
          while opt != "1" and opt != "2" and opt != "3":
            opt = input("""
1. Approach to fight 
2. Search for items
3. Leave
""")  
          if opt == "1":
            self.battle.battle(player, self.current_place.enemy)
            opt = ''
            while opt != "1" and opt != "2":
              opt = input("""
1. Search for items
2. Leave
""")
            if opt == "1":
              player.want_item(self.current_place)
              print("""
You decide to leave
""")
              self.move_place()
            elif opt == "2":
              print("""
You decide to leave
""")
              self.move_place()
          elif opt == "2":
            player.want_item(self.current_place)
            opt = ""
            while opt != "1" and opt != "2":
              opt = input("""
1. Approach to fight
2. Leave
""")  
            if opt == "1":
              self.battle.battle(player, self.current_place.enemy)
              print("""
You decide to leave the area
""")
              self.move_place()
            elif opt == "2":
              self.move_place()
          elif opt == "3":
            self.move_place()
        
        elif opt == "2":
          self.battle.battle(player, self.current_place.enemy)
          opt = ''
          while opt != "1" and opt != "2":
            opt = input("""
1. Search for items
2. Leave
""")
            if opt == "1":
              player.want_item(self.current_place)
              print("""
You decide to leave
""")
              self.move_place()
            elif opt == "2":
              print("""
You decide to leave
""")
        elif opt == "3":
          player.want_item(self.current_place)
          opt = ''
          while opt != "1" and opt != "2":
            opt = input("""
1. Approach to fight
2. Approach to talk
""")
          if opt == "1":
            self.battle.battle(player, self.current_place.enemy)
            self.move_place()
          elif opt == "2":
            self.current_place.enemy.chat()
            opt = ''
            while opt != "1" and opt != "2":
              opt = input("""
1. Approach to fight
2. Leave
""")
            if opt == "1":
              self.battle.battle(player, self.current_place.enemy)
              self.move_place()
            elif opt == "2":
              self.move_place()
              
              
            
            
            

    
      else:
        if self.current_place.enemy.defeated == True:
          time.sleep(0.5)
          print("You search for items")
          player.want_item(self.current_place)
          print("You decide to leave")
          self.move_place()
        else:
          opt = input("""
1. Approach to talk
2. Approach to fight
3. Search for items
""")
          while opt != "1" and opt != "2" and opt != "3":
            opt = input("""
  1. Approach to talk
  2. Approach to fight
  3. Search for items
  """)   
          if opt == "1":
            self.current_place.enemy.chat()
            self.current_place.enemy.talk = True
            opt = ''
            while opt != "1" and opt != "2" and opt != "3":
              opt = input("""
  1. Fight 
  2. Search for items
  3. Leave
  """)  
            if opt == "1":
              self.battle.battle(player, self.current_place.enemy)
              opt = ''
              while opt != "1" and opt != "2":
                opt = input("""
  1. Search for items
  2. Leave
  """)
              if opt == "1":
                player.want_item(self.current_place)
                print("""
  You decide to leave
  """)
                self.move_place()
              elif opt == "2":
                print("""
  You decide to leave
  """)
            elif opt == "2":
              player.want_item(self.current_place)
              opt = ""
              while opt != "1" and opt != "2":
                opt = input("""
  1. Fight
  2. Leave
  """)  
              if opt == "1":
                self.battle.battle(player, self.current_place.enemy)
                print("""
  You decide to leave the area
  """)
                self.move_place()
              elif opt == "2":
                self.move_place()
            elif opt == "3":
              self.move_place()
          
          elif opt == "2":
            self.battle.battle(player, self.current_place.enemy)
            opt = ''
            while opt != "1" and opt != "2":
              opt = input("""
  1. Search for items
  2. Leave
  """)
              if opt == "1":
                player.want_item(self.current_place)
                print("""
  You decide to leave
  """)
                self.move_place()
              elif opt == "2":
                print("""
  You decide to leave
  """)
          elif opt == "3":
            player.want_item(self.current_place)
            opt = ''
            while opt != "1" and opt != "2":
              opt = input("""
  1. Fight
  2. Talk
  """)
            if opt == "1":
              self.battle.battle(player, self.current_place.enemy)
              self.move_place()
            elif opt == "2":
              self.current_place.enemy.chat()
              opt = ''
              while opt != "1" and opt != "2":
                opt = input("""
  1. Fight
  2. Leave
  """)
              if opt == "1":
                self.battle.battle(player, self.current_place.enemy)
                self.move_place()
              elif opt == "2":
                self.move_place()
          
    def start(self):
        import time
        name = input("Enter player name: ")
        player = Player(name)
        print("Welcome to my game...")
        time.sleep(1)
        print("""
IMPORTANT INFO:
YOUR STATS:

You have 5 stats:
Speed - The higher your speed is the more likely that you will move first in a turn in combat.
Defense - Reduces the amount of damage you take. Your defense can only go up to 100.
Base Attack - Affects how much damage you do. Using items will increase damage too. If you do not use an attack item, your base attack will be used as your damage.
Energy - You need energy to use weapons. Some weapons take more energy than others.
Health - If your health reaches 0, you lose.
Your enemies will have these stats too.
After winning a battle, your health and energy will be restored to their maximum values.
""")
        time.sleep(4)
        print("""
TRAINING:
Every time you enter a new place, you will be able to train. If you pass the training minigame in 3 attempts or under, you can upgrade a stat.

REWARDS FOR BATTLES:
Also you have a maximum inventory size that you can carry. To increase your inventory size you will have to win battles. After battles you will also increase you stats.

""")
        time.sleep(3)
        
        print("Your family is struggling, so you decide you embark on a journey to find the legendary treasure. You are given some items by family to help you during your journey." """

""")
        time.sleep(2)
        print("Your brother gives you some medicine. It healing effect " + str(self.medicine.heal) + ", it has a durability of " + str(self.medicine.durability) + " and has a size of " + str(self.medicine.size))
      
        player.add_item(self.medicine)
        time.sleep(2)
      
        print("Your mother gives you a sword. Its attack is " + str(self.sword.damage) + ", has a durability of " + str(self.sword.durability) + ", has a size of " + str(self.sword.size) + " and takes " + str(self.sword.energy_taken) + " energy to use")
      
        player.add_item(self.sword)
        time.sleep(2)
      
        print("Your father gives you his legendary spear called 'One Shot'. Its attack is " + str(self.one_shot.damage) + ", has a durability of " + str(self.one_shot.durability) + ", has a size of " + str(self.one_shot.size) + " and takes " + str(self.one_shot.energy_taken) + " energy to use")
        player.add_item(self.one_shot)
        
        print("You then go outside")
        time.sleep(0.5)
        
        print("You are currently in " + self.current_place.name)

        time.sleep(0.5)

        print("""
After leaving, you decide to search around the nearby area for more items.
""")
        time.sleep(0.5)
        
        player.want_item(self.home)
      
        player.check_inventory()

        self.train.train(player)
        
        self.map.show_map()
      
        d = False
        while d == False:
          self.current_place.show_next_places()
          next_place = input("""
Enter next place
""")      
          if next_place in self.current_place.next_places_name:
            i = 0
            while next_place != self.current_place.next_places[i].name:
              i = i + 1
            d = True
        self.current_place = self.current_place.next_places[i]
        time.sleep(1)
        print("""
""""Before you can leave, your brother challenges you to a fight" """
'I have to make sure that you're ready', he says.
""")
        player.check_inventory()
        self.battle.battle(player,self.brother)
        print("Current place:" + str(self.current_place.name))

        while self.Dragon.defeated == False:
          self.enter_place(player)
        
        if self.Timmy.defeated == False:
          print("""
You defeated the dragon
""")
          time.sleep(0.5)
          print("You see a chest filled to the brim with gold and expensive jewels")
          time.sleep(0.5)
          print("But as you go to grab it...""""
""")
          time.sleep(1)
          print("A small figure leaps out the shadows and takes it. The last thing you hear is: 'You won't catch Timmy!' as the figure slips back to the shadows.")
          time.sleep(1)
          print("""
You stand frozen in disbelief for a while. You cannot believe what just happen. Unfortunately, you return home empty-handed as your family are still struggling financially.
You think about what could have been if Timmy never had the opportunity to take your treasure...""")
        elif self.Thief.defeated == False:
          print("""
You find a treasure chest filled to the brim with gold and jewels. You grab it and begin your journey back home.
""")
          time.sleep(0.5)
          print("""However, during your journey back, a thief grabs the chest from your arms and takes the chest. Some of the treasure spilt out of the chest as the thief runs away. You are able to collect the spilt treasure, and it is enough to support your family for a while. 
You wonder about what could have been if you had made sure the thief never had a chance to steal your treasure...""")
        elif self.TreasureHunter.defeated == False:
          time.sleep(0.5)
          print("""
You find a treasure chest filled to the brim with gold and jewels but before you could even reach out for it...
""")
          time.sleep(0.75)
          print("""A man runs and grabs the treasure chest with both hands. He turns to you and says with a smile 'I've had my eye on this treasure for a while. Thanks for defeating the dragon for me. Too bad that you'll get nothing for it.'
You try to grab it back immediately but he sees your desperate lunge at him coming and he evades you and disappears. You return home empty-handed and your family still are struggling financially.
If only you had defeated that Treasure Hunter earlier...""")
          
        else:
          time.sleep(0.5)
          print("""
You find a massive treasure chest filled to the brim with gold and jewels.
""")
          time.sleep(0.5)
          print("You quickly grab the heavy chest and return home")
          time.sleep(0.5)
          print("The treasure is more than enough to support your family for multiple lifetimes. You and your family now happily live a life of luxury. Word spreads throughout the land about how you obtained the treasure, and you are treated as a king wherever you go.")
      


game = Game()
game.setup()
game.start()
