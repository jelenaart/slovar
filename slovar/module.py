from random import *
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


def viga():
    print("not done")

def translate():
    print("not done")

def engest(f:str,eesti:list):
   while True:
       try:
           word=input("What word would you like to translate?")
           if word in english:
               #
            if word in estonian:
                print("Tundub et see on eesti sõna. Soovite avada teist sõnastikut ning tõlkida seda inglise keele? 1-jah; 2-ei")
                if valik==1:
                    esteng()
                if valik==2:
                    break

def esteng(english:list,eesti:list):
    while True:
        try:
            word=input("Mis sona soovite tolkida?")
           if word in english:
                print("Tundub et see on eesti sõna. Soovite avada teist sõnastikut ning tõlkida seda inglise keele? 1-jah; 2-ei")
                if valik==1:
                    engest()
                if valik==2:
                    break
            if word in estonian:
                #
        except ValueError:
            print("Try again")
               

def uussona(f:str,rida:str)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
        l=failist_lugemine(f)
        return l