#Class Methods
#From Video #61

class Animal:
    kindome = "Mamuls"
    powers = {
        'speed kmh' : 25
    }
    color = ['white', 'black','brown']
    
    def myMethod(self):
        print(self.powers)
    
    def get_speed(self):
        spd = self.powers['speed kmh']
        return spd

    def add_color(self, color):
        self.color.append(color)

    @property        #This Method is treated as a properties
    def get_color_list(self):
        return self.color

animal = Animal()
animal.myMethod()
anmlSpd = animal.get_speed()
print("This animal speed is",anmlSpd,'Kmh')

colurs = animal.get_color_list
print(colurs)

animal.add_color('Beage')
colurs = animal.get_color_list
print(colurs)

# print(animal.kindome)
# print(animal.powers)
# print(animal.color[0])
# print(animal._private_test)
