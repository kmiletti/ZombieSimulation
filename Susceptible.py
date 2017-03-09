from Person import *

class Susceptible():
    def __init__(self, name, x, y):
        '''Return a susceptible person whose name is name and whose coordinates are x, y'''
        self.name = name
        self.x = x
        self.y = y

    def walk(self):
        return 0

    def forage(self):
        return 0