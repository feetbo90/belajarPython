
bil1 = input("Masukkan bilangan : ")
bil2 = input("Masukkan bilangan 2 : ")
bil3 = input("Masukkan bilangan 3 : ")

bilangan1 = int(bil1)
bilangan2 = int(bil2)
bilangan3 = int(bil3)

# cara I
if bilangan1 > bilangan2:
    if bilangan1 > bilangan3 :
        print(bilangan1)
    else :
        print(bilangan3)
elif bilangan2 > bilangan3 :
    print(bilangan2)
else :
    print(bilangan3)

# cara II
if bilangan1 > bilangan2 and bilangan1 > bilangan3 :
    print(bilangan1)
elif bilangan2 > bilangan3 :
    print(bilangan2)
else :
    print(bilangan3)

