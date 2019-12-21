"""
Melakukan tukar nilai A, B, C, D menjadi B,D,A,C jika A,B,C,D bilangan desimal

"""

A = input("Masukkan nilai A dengan desimal ")
print(type(A))
B = input("Masukkan nilai B dengan desimal ")
C = input("Masukkan nilai C dengan desimal ")
D = input("Masukkan nilai D dengan desimal ")

if isinstance(float(A),float) and isinstance(float(B),float) and isinstance(float(C),float) and isinstance(float(D),float) :
    temp = A
    A = B
    B = D
    temp2 = C
    C = temp
    D = temp2

print("maka nilai A : " + A)    
print("maka nilai B : " + B)
print("maka nilai C : " + C)
print("maka nilai D : " + D)



