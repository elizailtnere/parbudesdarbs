class Darzs:
    def __init__(produkts, nosaukums, skaits, veids = 0 ):
        produkts.nosaukums = nosaukums
        produkts.skaits = skaits
        produkts.veids = veids
    
    def svinet_dz_d(produkts):
        produkts.skaits += 1
        produkts.info()
    
    def mainit_vardu(self, jaunais_vards):
        self.vards = jaunais_vards
        self.info()
    
    def mainit_dzimumu(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.dzimums == "s":
                self.dzimums = "v"
            else:
                self.dzimums = "s"
        else:
            self.dzimums = jaunais_dzimums
        self.info()

    def info(produkts):
        # print("Sveiki, mani sauc", self.vards)
        # print("Man ir", self.vecums, "gadu.")
        # if self.dzimums == "s":
        #     print("Es esmu sieviete")
        # elif self.dzimums == "v":
        #     print("Es esmu vīrietis")
        # else:
        #     print("Es esmu", self.dzimums)
        if produkts.nosaukums == "v":
            teksts = "vīrietis"
        elif produkts.skaits == "s":
            teksts = "sieviete"
        else:
            teksts = produkts.veids
        print("Sveiki, mani sauc {}. Man ir {} gadu, es esmu {}.".format(produkts.nosaukums, produkts.skaits, teksts))
        return ("Sveiki, mani sauc {}. Man ir {} gadu, es esmu {}.".format(produkts.nosaukums, produkts.skaits, teksts))

    def __del__(produkts):   #Kas papildu jāizdara pirms objektu iznīcina, izmantojot del
        print("Visu labu!")
    



