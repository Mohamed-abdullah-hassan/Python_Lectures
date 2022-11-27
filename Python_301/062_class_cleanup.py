#Class Cleanup
#From Video #62

class Animal:
    kindome = "Mamuls"
    powers = {
        'speed kmh' : 25
    }
    color = ['white', 'black','brown']
    
    def sound(self):
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
