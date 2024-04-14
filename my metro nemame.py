#vlozenie modulu
import tkinter

#nastavanie platna
canvas = tkinter.Canvas(width=1000, height=300, background="white")
canvas.pack()

#otvorenie suboru
subor = open("trasa_linky_metra.txt","r")

#zistenie farby
farba = subor.readline()
farbicka = farba.strip()

#precitanie prveho riadku
suborik = subor.readlines()

#zistenie dlzky suboru
dlzka = len(suborik)

#nastavenie povodnych suradnic
x = 20
x1 = 20
x2 = 55

def vykreslenie(): #funkcia na vykreslenie
    #zadefinovanie globalnych hodnot
    global x,x1,x2
    global farbicka

    #zadeklarovanie pomocnej premennej
    pocet = 0

    for riadok in suborik: #cyklus na prechadzanie riadkov v subore
        #vypisanie zastavky
        canvas.create_text(x2,150,text=riadok,font="Arial 8",angle=45)

        #podmienka na vykreslenie kruzku/stvorceka
        if pocet == 0:
            canvas.create_rectangle(10,200,20,190,fill=farbicka,outline="")
            canvas.create_line(x1,195,x1+30,195,fill=farbicka)
        elif pocet == dlzka-1:
            canvas.create_rectangle(36*(dlzka-1),200,(36*(dlzka-1))+10,190,fill=farbicka,outline="")

            #ukoncenie funkcie
            return
        elif riadok[0] == "*":
            canvas.create_oval(x+30,200,x+40,190,fill="white",outline=farbicka)
            canvas.create_line(x1+5,195,x1+30,195,fill=farbicka)

            #zmena suradnice
            x += 35
        else:
            canvas.create_oval(x+30,200,x+40,190,fill=farbicka,outline="")
            canvas.create_line(x1+5,195,x1+30,195,fill=farbicka)

            #zmena suradnice
            x += 35

        #zmena suradnic
        x1 += 35
        x2 += 35

        #zmena pomocnej premennej
        pocet += 1

#zavolanie funkcie
vykreslenie()

#dokreslenie ciary
canvas.create_line(x,195,x+35,195,fill="red")

#zatvorenie suboru
subor.close()
