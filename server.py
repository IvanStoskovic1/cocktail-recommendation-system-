import socket
from tkinter import *
import sqlite3
from tkinter import messagebox
import threading
import time
import json
PORT=55001
HOST=socket.gethostname()

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.bind((HOST,PORT))
serv.listen()
print("Server...")
top=Tk()
top.geometry("600x600")
top.title("Izbor Koktela server")


def vremeTece():
    while True:
        val_vreme.set(time.ctime(time.time()))
        time.sleep(1)



def prihvati():
    while True:
        konekcija = sqlite3.connect('bazakoktela.db')
        cursor = konekcija.execute("SELECT ime,sastojci,jacina,ukus from kokteli")
        conn, addr = serv.accept()
        print("Adresa od klijenta: ", addr)
        poruka = conn.recv(1024).decode()

        poruka = poruka.split('|')

        max_poeni = 0
        koktel_max =[]
        for row in cursor:
            ntrorkaKoktela = (row[0], row[1], row[2], row[3])
            poeni = 0
            sastojci_koktela = ntrorkaKoktela[1].split(",")
            for sastojak in sastojci_koktela:
                if sastojak.strip() in poruka[0]:
                    poeni += 1
            if ntrorkaKoktela[2] in poruka[1]:
                poeni += 1
            if ntrorkaKoktela[3] in poruka[2]:
                poeni += 1

            if poeni > max_poeni and poeni>0:
                max_poeni = poeni
                koktel_max = [ntrorkaKoktela[0]]
            elif poeni==max_poeni and poeni>0:
                koktel_max.append(ntrorkaKoktela[0])
        if koktel_max:
            ispisKoktela=", ".join(koktel_max)
        else:
            ispisKoktela="Nema rezultata"
        val_poruka.set("Odgovor poslat na klijent")
        f=open("ispis.txt","a",encoding="utf-8")
        f.write(f"{time.ctime()} - {ispisKoktela}\n")
        f.close()
        odgovor = {
            "rezultat": ispisKoktela,
            "vreme": time.ctime()
        }

        json_odgovor = json.dumps(odgovor)

        conn.send(json_odgovor.encode())
        conn.close()
        konekcija.close()
val_vreme = StringVar()
threading.Thread(target=vremeTece).start()
labelaVreme = Label(top, textvariable=val_vreme)
labelaVreme.pack()
val_poruka = StringVar()
labelaPoruka = Label(top, textvariable=val_poruka,font=("Verdana", 9, "bold"))
labelaPoruka.pack()
threading.Thread(target=prihvati).start()
top.mainloop()




