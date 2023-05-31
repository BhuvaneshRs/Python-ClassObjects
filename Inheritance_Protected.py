class fruits():
    def __init__(self,name,kg,vitamin):
        self.name=name
        self.kg=kg
        self._vitamin=vitamin
    def fruitsdisplay(self):
        print(f"Name={self.name}")
        print(f"KiloGram={self.kg}")
        print(f"Vitamin={self._vitamin}")

class Vegetables(fruits):
    def getVegetable(self,vname,vkg):
        self.__vname=vname
        self.vkg=vkg
    def vegetabledisplay(self):
        print(f"vname={self.__vname}")
        print(f"Vegetable Kilogram={self.vkg}")
        print(f"Vegetable Vitamin={self._vitamin}")

class seeds(Vegetables):
    def getseeds(self,sname,sprice):
        self.sname=sname
        self.sprice=sprice
    def seedsdisplay(self):
        print(f"Seed Name={self.sname + 'Seed'}")
        print(f"Seed price={self.sprice}")
        print(f"Seed Vitamin={self._vitamin}")

eatable1=seeds("apple",4,"A")
eatable1.getVegetable("Carrot",4)
eatable1.getseeds("apple",160)


#Output:
eatable1.fruitsdisplay()
Name=apple
KiloGram=4
Vitamin=A

eatable1.vegetabledisplay()
vname=Carrot
Vegetable Kilogram=4
Vegetable Vitamin=A

eatable1.seedsdisplay()
Seed Name=appleSeed
Seed price=160
Seed Vitamin=A
