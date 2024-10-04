from augliundarzeni import darza_produkti

produktu_saraksts = []

for i in range(20):
    produktu_saraksts.append(Sieviete("Anna","blonda", i))

for sieviete in cilveku_saraksts:
    if sieviete.vecums % 2 == 0:
        sieviete.mainit_dzimumu()

print ("-------------------")
for sieviete in cilveku_saraksts:
    sieviete.info()