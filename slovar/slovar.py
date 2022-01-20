from module import *
english=[]
eesti=[]
english=failist_lugemine('english.txt',english)
eesti=failist_lugemine('eesti.txt',eesti)

#valik=""
#while True:
#    try:
#        valik=int(input("Valige: (1)Tõlkida english-estonian\n(2)Tõlkida eesti-inglise\n(3)test yourselfNOT DONE\n(4)Leave"))
#        if valik==1:
#            engest()
#        elif valik==2:
#            esteng()
     
#        else:
#            print("Something went wrong. Please try again!")
#    except ValueError:
#        print("Try again please!")

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
            translate()
        elif menu.upper()=="L":
            break
        elif menu.upper()=="V":
            viga()
        else:
            print("Proovi veel kord")
    except ValueError:
        print("Midagi on valesti. Proovige veel kord!")
     