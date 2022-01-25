from module import *
english=[]
eesti=[]
english=failist_lugemine('english.txt',english)
eesti=failist_lugemine('eesti.txt',eesti)

while True:
    try:
        menu=input('Koik sonad - S, Tolgida-T, Uus sona-U, viga-V, kontroll-K,lopp-L')
        if menu.upper()=="U":
            eesti=uussona('eesti.txt',input("Uus sona"))
            english=uussona('english.txt',input("Uus sona"))

        elif menu.upper()=="S":
            print(english)
            print(eesti)
        elif menu.upper()=="T":
            translate(eesti,english)
        elif menu.upper()=="L":
            quit
            break
        elif menu.upper()=="V":
            viga(tolk,l)
        elif menu.upper()=="K":
            kontrol(eesti,english)
        else:
            print("Proovi veel kord")
    except ValueError:
        print("Midagi on valesti. Proovige veel kord!")
     
