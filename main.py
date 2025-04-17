class Pet:
    def __init__(self, name):
        # Initialize the pet's attributes here
        self.name = name
        self.hunger = 8
        self.energy = 5
        self.happiness = 5 
        self.tricks = []
        print(f"creating pet: {self.name}")

    def eat(self):
        # Implement the logic for the eat method
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate🍖 and feels a bit happier!")

    def sleep(self):
        # Implement the logic for the sleep method
        self.energy = min(10, self.energy + 5)
        self.happiness = max(0, self.happiness - 1)
        print(f"{self.name} had a good nap!💤")

    def play(self):
        # Implement the logic for the play method
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and had fun!🏐⚽")

    def get_status(self):
        # Implement the logic to print the pet's status
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10⚡")
        print(f"Happiness: {self.happiness}/10 🐱‍🏍")
        print("-" * (len(self.name) + 16))

    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!🤸🏽‍♀️")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.🐱")
