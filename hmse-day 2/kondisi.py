Telur = False

if (Telur):
    print("Beli 5")
else:
    print("Beli 1")

Telur = True
Apel = False

if (Telur and Apel):
    print("Beli 5")
else:
    print("Beli 1") 

Telur = True
Apel = False

if (Telur or Apel):
    print("Beli 5")
else:
    print("Beli 1") 

nilai = 80
hasil = "Lulus" if nilai >=80 else "gagal"
print(hasil)

Telur = False
Apel = True


nilai = 80
hasil = "Lulus" if nilai >=80 else "gagal"
print(hasil)
if (Telur and Apel):
    print("Beli 5")
elif(Telur):
    print("Beli 3")  
elif(Apel):
    print("Beli 2")   
else:
    print("Beli 1")

