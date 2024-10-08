class Char:
  def __init__(self, given_name, health, speed, attack, energy, defense, special_move, normal_move_1, normal_move_2):
        self.name = given_name
        self.health = health
        self.speed = speed
        self.attack = attack
        self.energy = energy
        self.defense = defense
        self.special_move = special_move
        self.normal_move_1 = normal_move_1
        self.normal_move_2 = normal_move_2
        self.damage = 0
        self.defeated = False
        self.talk = False
  def show_stats(self):
    import time
    time.sleep(0.5)
    print(self.name + "'s health: " + str(self.health))
    time.sleep(0.5)
    print(self.name + "'s energy: " + str(self.energy))
    time.sleep(0.5)
    print(self.name + "'s speed: " + str(self.speed))
    time.sleep(0.5)
    print(self.name + "'s defense: " + str(self.defense))
    time.sleep(0.5)
    print(self.name + "'s attack: " + str(self.attack))
  def rest(self):
    self.energy += 50
    print("Enemy rests and gains 50 energy")
  
  def see(self):
    import time
    if self.name == "Dragon":
      time.sleep(1)
      print("You see the Dragon")
    elif self.name == "Fly":
      time.sleep(1)
      print("You see a Fly")
    elif self.name == "Timmy":
      time.sleep(1)
      print("You see a kid")
    else:
      time.sleep(1)
      print("You see a person")


  
  def chat(self):
    if self.name == "Timmy":
      print("""'Hello there!' you yell to the kid. 'What's you name?'
'My name is Timmy'
'Do you know anything about the treasure, Timmy?' you ask.
He smiles suspiciously.
'I don't know what you're talking about'.
""")
    if self.name == "Mystery Man":
      print("""
'Hello there sir! Have you heard anything about the treasure' you ask.
'No', he responses coldly.
""")
    if self.name == "Fly":
      print("""
You try to speak with the fly
It only responds with 'Bzzt' 
""")
    if self.name == "Castle Protector":
      print("""
'Hello sir! Do you know anything about the treasure?', you ask.
'I would go home now if I were you, you would have to defeat the dragon in castle, and it is impossibly strong.'
'I have my reasons to continue onwards', you reply.
'Best of luck to you', the man responds.
""")
    if self.name == "Regular Guy":
      print("""
'Hello!' you say to the man. 'Have you heard about any treasure?'
'Hmmm...' he starts, 'my grand-parents always told stories about a treasure in the castle. I believe that the stories are myth though'
""")
    if self.name == "Castle Defender":
      print("""
'Hel-', you start, but the man cuts you off.
'Get out of my sight', he says with no emotion on his face
""")
    if self.name == "Thief":
      print("""
'Hello Sir. Have you heard any-'
The man starts running off before you can finish your question.
The village people then tell you that he is an infamous thief in the area.
""")
    if self.name == "Treasure Hunter":
      print("""
'Hello sir! Have heard anything about some treasure?', you ask.
He chuckles
'As if I would tell you anything. That treasure's going to be all mine.'
""")
    if self.name == "Dragon":
      print("""
'Hello Dragon!', you say.
It isn't facing you and it doesn't respond
""")
    