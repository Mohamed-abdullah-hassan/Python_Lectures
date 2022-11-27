#OOP Dunder method
#From Video #66
#Dunder = Double Underscore which means class initilizer

class Animal:
    
    def __init__(self, height = '180 cm' ):
        self.height = height
    
    kingdome = "Animal"

    powers = {
        'speed kmh' : 25
    }
    color = ['white', 'black','brown']
    origin = 'Africa'
    
    def sound(self):
        print("I can Run Fast",self.powers)
    
    def get_speed(self):
        spd = self.powers['speed kmh']
        return spd

    def food(self,animal = 'Lion', food='Gazzal'):
        print(f"a {animal} favorite food is: {food} ")

    def add_color(self, color):
        self.color.append(color)
        self.color.sort()
    
    def print_Colors(self):
        print(self.color)
        # forcing inheriting class to implemnt this method like virtual in c 
        # raise NotImplementedError

    @property        #This Method is treated as a properties
    def get_color_list(self):
        return self.color
    

class Tiger(Animal):
    color = ['white', 'black']

    def __init__(self):
        super().__init__('110 cm')

    def sound(self):
        print("Awoooooooooooooooooooooo")

    def print_Colors(self):
        print("Tiger Colors are:",self.color)

    def food(self):
        super().food('Tiger', 'Cows')
        print("Tigers are very fast")


class Cat(Animal):
    color = ['Green','Sandy', 'Brown','Greay']

    def __init__(self, color):
        super().__init__('18 cm')
        self.origin = 'Egypt'
        self.color.append(color)
        self.color.sort()

    def sound(self):
        print("Meow!!")

    def food(self):
        super().food('Cat', 'Mices')
        print("Cats play to much")
    
    def print_Colors(self):
        print("Cats Colors are:",self.color)

animal = Animal()
tiger = Tiger()
cat = Cat('Orange')



print("\nPrinting Height of each animal")
print(animal.height)
print(tiger.height)
print(cat.height)

print("\nPrinting Color for each animal")
animal.print_Colors()
tiger.print_Colors()
cat.print_Colors()
