#OOP Super() method
#From Video #65

class Animal:
    kindome = "Mamuls"
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
        # print(self.color)
        # forcing inheriting class to implemnt this method like virtual in c 
        raise NotImplementedError

    @property        #This Method is treated as a properties
    def get_color_list(self):
        return self.color
    

class Tiger(Animal):
    color = ['white', 'black']
    def sound(self):
        print("Awoooooooooooooooooooooo")

    def print_Colors(self):
        print("Tiger Colors are:",self.color)

    def food(self):
        super().food('Tiger', 'Cows')
        print("Tigers are very fast")


class Cat(Animal):
    color = ['Brown','Orange', 'Green','Sandy']
    def sound(self):
        print("Meow!!")

    def food(self):
        super().food('Cat', 'Mices')
        print("Cats play to much")

animal = Animal()
tiger = Tiger()
cat = Cat()



print("\nPrinting Types of each calss")
print(type(animal))
print(type(tiger))
# print(type(cat))

print("\nPrinting color from each calss")
# animal.print_Colors()
tiger.print_Colors()
# cat.print_Colors()
print(' ')

tiger.food()

print('')
cat.food()
