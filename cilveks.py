class Produkti:
    def __init__(self, nosaukums, veids, skirne, skaits = 0 ):
        self.skaits = skaits
        self.nosaukums = nosaukums
        self.veids = veids
        self.skirne = skirne 

    def info(self):
    
        if self.veids == "a":
            teksts = "Auglis"
        elif self.veids == "d":
            teksts = "Dārzenis"
        else:
            teksts = self.veids
            print("{}, {}, {}, {}.".format(self.nosaukums, self.skaits, self.skirne, teksts))
            return "{}, {}, {}, {}.".format(self.nosaukums, self.skaits, self.skirne, teksts)
    
    def __del__(self):  
        print("Visu labu!")
