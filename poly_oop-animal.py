class Dog:
    def move(self):
        print("Running 🐶")

class Bird:
    def move(self):
        print("Flying 🦅")

class Fish:
    def move(self):
        print("Swimming 🐟")

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()
