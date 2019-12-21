bilA = input("Masukkan bilangan A : ")
bilB = input("Masukkan bilangan B : ")
bilC = input("Masukkan bilangan C : ")
bilD = input("Masukkan bilangan D : ")

# print(bilA)
# print(bilB)
# print(bilC)
# if bilA > bilB:
#     if bilA > bilC : 
#         print("paling besar : ")
#         print(bilA)
#     else :
#         print("paling besar : ")
#         print(bilC)
# elif bilB > bilC :
#     print("paling besar : ")
#     print(bilB)
# else :
#     print("paling besar : ")
#     print(bilC)
# bilA = 100
# bilB = 70
# bilC = 80
# bilD = 90
if bilA > bilB:
    if bilA > bilC : 
        print("paling besar : ")
        print(bilA)
    else :
        print("paling besar : ")
        print(bilC)
elif bilB > bilC :
    print("paling besar : ")
    # print(bilB)
    if bilB > bilD:
        print(bilB)
    else :
        print(bilD)
elif bilC > bilD :
    print("paling besar : ")
    print(bilC)
else:
    print(bilD)

    
