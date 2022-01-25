import random
def failist_lugemine(f:str,l:list):
    """Info failist f listisse l
    """
    fail=open(f,'r') #,encoding="utf-8-sig" #rezim 4teniya togo 4to v faile
    for rida in fail:
        l.append(rida.strip()) #'\n'
    fail.close()
    return l
def salvestamine(f:str,l:list):
    """Loetelu salvestamine failisse
    """
    fail=open(f,'w')#rezim perezapisi
    for el in l:
        fail.write(el+'\n')
    fail.close()

def ridasalv(f:str,rida:str):
    """Uks sona voi lause(rida) salvestamine failisse
    :param: fail kuhu salvestame
    :param str rida: sõna, mis vaja salvestada failisse
    """
    fail=open(f,'a')#rezim dozapisi
    fail.write(rida+'\n')
    fail.close()

def translate(eesti:list,english:list):
    tolk=input("Palun kirjutage sõna, mida te soovite tõlkida: ")
    if tolk in eesti:
        tolk=english[eesti.index(tolk)]
        print(tolk+"-"+tolk)
    elif tolk in english:
        tolk=eesti[english.index(tolk)]
        print(tolk+"-"+tolk)
    else:
        print("Midagi on valesti. Võib olla seda sõna pole veel lisatud!")


def viga(tolk:str,l:list):
    for i in range(len(l)):
        if l[i]==tolk:
            uus_sona=tolk.replace(tolk,input("Uus sona"))
            l.insert(i,uus_sona)
            l.remove(tolk)
    return l

def heli(text:str,keel:str):
	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
	os.system("heli.mp3")

               

def uussona(l:str,f:str,rida:str)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
        l=failist_lugemine(f)
        return l

def kontrol(eesti:list,english:list):
    l=[]
    l.extend(eesti)
    l.extend(english)
    random.shuffle(l)
    print("Kontrolli oma teadmusi",l)
    p=False
    for i in range(len(eesti)):
        print(eesti)
        vastus=input("Palun tõlgi sõna ")
        if vastus.isalpha():
            p=True
        if vastus in eesti or english:
            p=True
        if l[i] in eesti:
            if eesti.index(l[i])==english(vastus):
                print("Oled tubli")
        elif l[i] in english:
            if english.index(l[i])==eesti(vastus):
                 print("Oled tubli")
        else:
            print("Midagi on vale")
    return p
