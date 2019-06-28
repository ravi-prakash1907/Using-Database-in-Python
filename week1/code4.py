#   Inheritance/Sub-class

class PartyAnimal:
    x = 0
    a = ''

    def __init__(self, z=''):
        print('I\'m constructor!')
        self.a = z

    def party(self):
        self.x = self.x + 1
        print("So far", self.x, self.a)


#       Inherits PartyAnimal
class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.a, "points", self.points)



an = PartyAnimal()

x = PartyAnimal('Jerry')
x.party()

y = FootballFan('Fan')
x.party()
y.party()
y.touchdown()
y.party()
