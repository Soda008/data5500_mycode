#class Pet:
#
#I was confused in my first code and now I know species should also be an variable
#
#    def __init__(self, name, age, species):
#        self.name = name
#        self.age = age
#        self.species = species.lower()

#    def pet_age_human(self):
#        species_multipliers = {
#            "dog": 7,
#            "cat": 6,
#            "fish": 20
#        }
#        multiplier = species_multipliers.get(self.species, 5)
#        return self.age * multiplier
#
#    def avg_lifespan(self):
#        species_lifespans = {
#        "dog": 10,
#        "cat": 15,
#        "fish": 3
#    }
#        return species_lifespans.get(self.species)
#
#Buddy = Pet("Buddy", 18, "dog")
#Whiskey = Pet("Whiskey", 2, "cat")
#Napoleon = Pet("Napoleon", 1, "fish")

##Chat suggested I loop the print functions
#for pet in [Buddy, Whiskey, Napoleon]:
#    print(pet.name, "is", pet.pet_age_human(), "in human years")
#    print("The average lifespan for a", pet.species, "is", pet.avg_lifespan())



class Pet:
    # species should be an attribute, not a class variable
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species.lower()

    def pet_age_human(self):
        species_multipliers = {
            "dog": 7,
            "cat": 6,
            "fish": 20
        }
        multiplier = species_multipliers.get(self.species, 5)
        return self.age * multiplier

    def avg_lifespan(self):
        species_lifespans = {
            "dog": 10,
            "cat": 15,
            "fish": 3
        }
        return species_lifespans.get(self.species)


# test code
Buddy = Pet("Buddy", 18, "dog")
Whiskey = Pet("Whiskey", 2, "cat")
Napoleon = Pet("Napoleon", 1, "fish")

for pet in [Buddy, Whiskey, Napoleon]:
    print(pet.name, "is", pet.pet_age_human(), "in human years")
    print("The average lifespan for a", pet.species, "is", pet.avg_lifespan())
