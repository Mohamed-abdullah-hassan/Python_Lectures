#Class Interface
#From Video #64

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

#Uncooment the Cat Class to show the error that print_Colors is not implemented in cat class
# class Cat(Animal):
#     # color = ['Brown','Orange', 'Green','Sandy']
#     def sound(self):
#         print("Meow!!")

# animal = Animal()
tiger = Tiger()
#Uncooment the following line to show the error that print_Colors is not implemented in cat class
# cat = Cat()



print("\nPrinting Types of each calss")
# print(type(animal))
print(type(tiger))
# print(type(cat))

print("\nPrinting color from each calss")
# animal.print_Colors()
tiger.print_Colors()
# cat.print_Colors()

