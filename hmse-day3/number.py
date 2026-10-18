import math
import random

#definisi variabel dengan tipe data number
x = 10      # int
y = 10.5    # float
z = 1j      # complex
z = 5

print("Nilai x:", x, "Tipe:", type(x))
print("Nilai y:", y, "Tipe:", type(y))
print("Nilai z:", z, "Tipe:", type(z))

# konversi tipe data
a = complex(int(float(x))) # convert int to float
b = int(y) # convert float to int
c = complex(x) # convert int to complex

print("\n--- hasil konversi ---")
print("int ke float:", a)
print("float ke int:", b)
print("int ke complex:", c)
