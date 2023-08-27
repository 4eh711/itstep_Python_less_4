# А якщо в конструктор класу треба передати вхідні
# параметри? Впоратись із цим допоможе запаковування
# параметрів. Самі ж *args та **kwargs треба передати
# як аргумент базового класу
class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model=model
        self.memory=128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution="4k"

class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)

iphone = SmartPhone(model="Last")
iphone.print_info()