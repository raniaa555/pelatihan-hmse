# cara 1
a = input("angka pertama")
b = input("angka kedua")

a,b = b,a
print("Hasil setelah ditukar")
print("a =", a) 
print("b =", b)

# cara 2
a = input("angka pertama")
b = input("angka kedua")

c = a
a = b
b = c
print("Hasil setelah ditukar")
print("a =", a) 
print("b =", b)
