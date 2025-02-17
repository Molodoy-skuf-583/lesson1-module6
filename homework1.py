class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):    
        if food.edible:
            self.fed = True
            print(f'{self.name} ate {food.name}')
        else:
            self.alive = False
            print(f'{self.name} did not eat {food.name}')


class Mammal(Animal):
    pass



class Predator(Animal):
    pass




class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True



class Flower(Plant):
    pass


a1 = Predator('Shark')
a2 = Mammal('Antelope')
p1 = Flower('Lemongrass')
p2 = Fruit('Banana')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)




