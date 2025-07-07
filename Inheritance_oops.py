class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Engine starts...")
    @staticmethod
    def stop():
        print("Engine stop...")
        
class ToyotaCar(car):
    def __init__(self,name):
        super().__init__(type)
        self.name=name
        self.start()
        

c1= ToyotaCar("mercedeez")
# c2= ToyotaCar("Toyota","Petrol Engine")
print(c1.name)
# print(c2.name,c2.type)
