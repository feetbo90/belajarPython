
# operator perbandingan
# >, <, >=, <=, ==, !=
# operator logika
# &&, ||
# and, or

# T   and     T       T
# T   and     F       F
# F T     F
# F F     F
#
# or
# T
# T
# T
# F

# if

# angka1 = input("masukkan bilangan 1: ")
# angka2 = input("masukkan bilangan 2: ")
#
# if angka1 > angka2:
#     print("maka bilangan terbesar :")
#     print(angka1)
# else :
#     print("maka bilangan terbesar :")
#     print(angka2)

nilai1 = input("Masukkan nilai 1 : ")
nilai2 = input("Masukkan nilai 2 : ")
nilai3 = input("Masukkan nilai 3 : ")
nilai4 = input("Masukkan nilai 4 : ")

jumlah = int(nilai1) + int(nilai2) + int(nilai3)+ int(nilai4)
nilaiRata = float(jumlah) / 4
print(nilaiRata)
# nilai >= 90
# A
# nilai >= 80 nilai < 90
# B+
# nilai < 80
# B
if nilaiRata >= 90 :
    print("A")
elif nilaiRata >= 80 and nilaiRata <90 :
    print("B+")
else :
    print("B")

# 280 190 100
# 280


