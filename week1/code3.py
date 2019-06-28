class PartyAnimal:
    x = 0
    a = ''

    def __init__(self, z=''):
        print('I\'m constructor!')
        self.a = z

    def party(self):
        self.x = self.x + 1
        print("So far", self.x, self.a)


#    def __del__(self):
#        print("Myself desturctor! Last val: ", self.x)


an = PartyAnimal()

x = PartyAnimal('Jerry')
x.party()

y = PartyAnimal('Tom')
x.party()
y.party()
