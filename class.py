class Dog:
    name = 'Tobby'
    
    def __init__(self):
        self.name = 'Blank'


obj = Dog()
print obj.name

obj.name = 'Toto'
print obj.name


class Doc(object):
   name = ''
   def __init__(self,name):
       self.name = name

a = Doc('Ruffles')
print a.name



class Cat(object):
    def __init__(self):
        print 'objeto instanciado'
    def miar(self, times):
        print 'mi' + 'a' * times + 'u'

class Siames(Cat):
    def rosnar(self):
        print 'rumpf'

c = Siames()
c.miar(3)
c.rosnar()