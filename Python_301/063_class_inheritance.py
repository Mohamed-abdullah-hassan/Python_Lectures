#Class Inheritance
#From Video #63

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

    def add_color(self, color):
        self.color.append(color)
        self.color.sort()
    
    def print_Colors(self):
        print(self.color)

    @property        #This Method is treated as a properties
    def get_color_list(self):
        return self.color
    

class Tiger(Animal):
    color = ['white', 'black']
    def sound(self):
        print("Awoooooooooooooooooooooo")

class Cat(Animal):
    # color = ['Brown','Orange', 'Green','Sandy']
    def sound(self):
        print("Meow!!")

animal = Animal()
tiger = Tiger()
cat = Cat()



print("\nPrinting Types of each calss")
print(type(animal))
print(type(tiger))
print(type(cat))
print("\nPrinting sound from each calss")
animal.sound()
tiger.sound()
cat.sound()

print("\nPrinting color from each calss")
animal.print_Colors()
tiger.print_Colors()
cat.print_Colors()

tiger.add_color("Orange on Black")
print("\nPrinting color from each calss after Adding Tiger color")
animal.print_Colors()
tiger.print_Colors()
cat.print_Colors()

print("\nPrinting color from each calss After Adding color to cat")
cat.add_color("Blak and White")
animal.print_Colors()
tiger.print_Colors()
cat.print_Colors()


print("\nPrinting Origen from each calss befor changing it in cat only")
print(animal.origin)
print(tiger.origin)
print(cat.origin)

cat.origin = "Egypt"

print("\nPrinting Origen from each calss after changing it in cat only")
print(animal.origin)
print(tiger.origin)
print(cat.origin)
