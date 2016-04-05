# Private Critter
# Demonstrates private variables and methods

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name                    # public attribute
        self.__mood = mood                  # private attribute

    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
