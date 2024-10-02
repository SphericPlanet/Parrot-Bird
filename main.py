class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is a {self.species} and its age is {self.age}")

blue = Parrot("Blue", 3)
blue.display()

woo = Parrot("Woo", 4)
woo.display()
