class PartyAnimal:
    x = 0
    a = ''

#    def __init__(self):
#        print('I\'m constructor!')

    def __init__(self, z=''):
        print('I\'m constructor!')
        self.a = z

    def party(self):
        self.x = self.x + 1
        print("So far", self.x, self.a)


    def __del__(self):
        print("Myself desturctor! Last val: ", self.x)


an = PartyAnimal()

an.party()
an.party()
an = 6
print("New", an)

x = PartyAnimal('Puppy')
x.party()
