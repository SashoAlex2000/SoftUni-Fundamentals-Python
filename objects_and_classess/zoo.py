class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = f""
        if species  ==  "mammal":
            result += f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}"
        elif species  ==  "fish":
            result += f"Fish in {self.name_of_zoo}: {', '.join(self.fishes)}"
        elif species  ==  "bird":
            result += f"Bird in {self.name_of_zoo}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"

        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for i in range(number_of_lines):
    current_animal = input().split(" ")
    species = current_animal[0]
    type_of_animal = current_animal[1]
    zoo.add_animals(species, type_of_animal)


additional_info = input()
print(zoo.get_info(additional_info))

