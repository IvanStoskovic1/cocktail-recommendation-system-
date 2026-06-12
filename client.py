import socket
from distutils.command.config import config
from tkinter import *
from tkinter import messagebox
import json
PORT=55001
HOST=socket.gethostname()

alkoholLista=[]
class Zahtev:
    def __init__(self,sastojci,jacina,ukus):
        self.sastojci=sastojci
        self.jacina=jacina
        self.ukus=ukus

def pretrazi():
    val_rezultat.set("")
    alkoholLista=[]
    jacinKoktela = ""
    ukusKoktela = ""
    rum=val_rum.get()
    votka=val_votka.get()
    gin=val_gin.get()
    tekila=val_tekila.get()
    liker=val_liker.get()

    if rum==1: alkoholLista.append("Rum")
    if votka==1:alkoholLista.append("Votka")
    if gin==1:alkoholLista.append("Gin")
    if tekila==1:alkoholLista.append("Tequila")
    if liker==1:alkoholLista.append("Liker")

    jacina=val_jacina.get()
    if jacina==1:jacinKoktela="Blago"
    elif jacina == 2: jacinKoktela="Srednje"
    elif jacina==3 : jacinKoktela="Jako"

    ukus=val_ukus.get()
    if ukus==1:ukusKoktela="Slatko"
    elif ukus == 2: ukusKoktela="Gorko"
    elif ukus==3 : ukusKoktela="Kiselo"
    zahtev=Zahtev(alkoholLista,jacinKoktela,ukusKoktela)
    poruka=f"{zahtev.sastojci}|{zahtev.jacina}|{zahtev.ukus}"
    print(f"Saljem: {poruka}")
    try:
        klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        klijent.connect((HOST, PORT))
        klijent.send(poruka.encode())
        odgovor = klijent.recv(1024).decode()
        podaci = json.loads(odgovor)
        val_rezultat.set(
             f'Preporuka: {podaci["rezultat"]}\n')
        klijent.close()
    except:
        val_rezultat.set("Greska, nije dostupan server")



def obrisiIzborJacine():
    val_jacina.set(0)
def obrisiIzborUkus():
    val_ukus.set(0)

top=Tk()
top.geometry("600x600")


top.title("Izbor Koktela klijent")
naslov=Label(top,text="Preporuka koktela",font=("Verdana", 11, "bold"))
naslov.pack()
izborAlkohola=Label(top,text="Izbor alkohola",font=("Verdana", 9, "bold"))
izborAlkohola.pack()

val_rum=IntVar()
checkRum=Checkbutton(top,text="Rum",variable=val_rum,onvalue=1,offvalue=0)
checkRum.pack()

val_votka=IntVar()
cheVotka=Checkbutton(top,text="Votka",variable=val_votka,onvalue=1,offvalue=0)
cheVotka.pack()

val_gin=IntVar()
cheGin=Checkbutton(top,text="Gin", variable=val_gin,onvalue=1,offvalue=0)
cheGin.pack()

val_tekila=IntVar()
cheTekila=Checkbutton(top,text="Tequila",variable=val_tekila,onvalue=1,offvalue=0)
cheTekila.pack()

val_liker=IntVar()
cheLiker=Checkbutton(top,text="Liker",variable=val_liker,onvalue=1,offvalue=0)
cheLiker.pack()

izborJacine=Label(top,text="Izbor jacine", font=("Verdana", 9, "bold"))
izborJacine.pack()

val_jacina=IntVar()

radBlago=Radiobutton(top,text="Blago",variable=val_jacina,value=1)
radBlago.pack()

radSrednje=Radiobutton(top,text="Srednje",variable=val_jacina,value=2)
radSrednje.pack()

radJako=Radiobutton(top,text="Jako",variable=val_jacina,value=3)
radJako.pack()
dugmeObrisiJacinu=Button(top,text="Obrisi izbor",command=obrisiIzborJacine)
dugmeObrisiJacinu.pack()

izborUkusa=Label(top,text="Izbor ukusa",font=("Verdana", 9, "bold"))
izborUkusa.pack()

val_ukus=IntVar()

radSlatko=Radiobutton(top,text="Slatko",variable=val_ukus,value=1)
radSlatko.pack()

radKiselo=Radiobutton(top,text="Kiselo",variable=val_ukus,value=2)
radKiselo.pack()

radGorko=Radiobutton(top,text="Gorko",variable=val_ukus,value=3)
radGorko.pack()
dugmeObrisiUkus=Button(top,text="Obrisi izbor",command=obrisiIzborUkus)
dugmeObrisiUkus.pack()
dugmePretrazi=Button(top,text="Pretrazi",command=pretrazi)
dugmePretrazi.pack()

val_rezultat=StringVar()
labelaRezultat=Label(top,textvariable=val_rezultat,font=("Ariel", 11, "bold"))

labelaRezultat.pack()



top.mainloop()






