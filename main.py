class Computer:
    def calculate(self):
        print("Calculating...")

class Display:
    def display(self):
        print("I display the image on the screen")

class SmartPhone(Computer,Display):
    pass

iphone = SmartPhone()
iphone.calculate()
iphone.display()