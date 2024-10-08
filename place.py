class Place():
    def __init__(self, given_name, enemy):
        self.name = given_name
        self.next_places = []
        self.next_places_name = []
        self.items = []
        self.enemy = enemy
        self.enter = False

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)
        self.next_places_name.append(place_instance.name)

    def add_item(self, item_instance):
        self.items.append(item_instance)

    def remove_item(self, item_instance):
        self.items.remove(item_instance)

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            print(place.name)
