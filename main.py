"""
COMP.CS.100.
Tekijä: Taavi Häkkinen
Opiskelijanumero: 151327111
"""
import copy
from tkinter import *
import time
import threading
import random



class Userinterface:
    def __init__(self):

        self.__mainwindow = Tk()

        self.__ennatykset = []

        self.build_menu()



    def build_menu(self):

        self.clear_the_screen()


        self.__mainwindow.title("Nappaa tonttu!")
        self.__mainwindow.geometry("600x400")
        self.__mainwindow.configure(bg="azure4")

        self.__otsikko = PhotoImage(file="otsikko.png")
        self.__otsikko_label = Label(image=self.__otsikko,bg="azure4")
        self.__startbutton = Button(self.__mainwindow,text="Aloita",command = self.get_player_details,font="Fixedsys")
        self.__highscoresbutton = Button(self.__mainwindow, text="Ennätykset",command=self.build_highscores,font="Fixedsys")
        self.__quitbutton = Button(text="Quit game",font="Fixedsys", command= self.stop)

        self.__otsikko_label.pack(pady=(20,0))
        self.__startbutton.pack(ipadx=43,ipady=10,pady=(30,0) )
        self.__highscoresbutton.pack(ipadx=30, ipady=10,pady=(10,0))
        self.__quitbutton.pack(ipadx=31, ipady=10,pady=(10,0))


    def clear_the_screen(self):

        for widget in self.__mainwindow.winfo_children():
            widget.destroy()


    def get_player_details(self):


        self.clear_the_screen()


        self.__namelabel = Label(text="Lisää pelaajatunnus",bg="azure4",font=("Fixedsys",16))
        self.__playername = Entry(font="Fixedsys")
        self.__startgamebutton = Button(text="Aloita",command = self.buildgame,font="Fixedsys")
        self.__takaisinbutton = Button(text="Takaisin", command=self.build_menu, font=("Fixedsys"))

        self.__takaisinbutton.pack(anchor="w", side="bottom")
        self.__namelabel.pack(ipadx=42,ipady=10,pady=(120,0) )
        self.__playername.pack(pady = (10,0))
        self.__startgamebutton.pack(ipadx=31, ipady=10,pady=(10,0))





    def buildgame(self):



        #Tallennetaan pelaajan ennen päävalikko ruudun tyhjennystä
        self.__playernamestr = copy.deepcopy(self.__playername.get())
        #Palataan takaisin menuun jos nimikenttä on tyhjä
        if len(self.__playername.get()) == 0:
            return

        self.clear_the_screen()


        for widget in self.__mainwindow.winfo_children():
            widget.destroy()

        self.__tonttu = PhotoImage(file="tonttu5.png")
        self.__filler = PhotoImage(file="transparent.png")

        self.__fillerlabel = Label()
        self.__button1 = Button(self.__mainwindow,background="azure4",command=self.button1_pressed,image=self.__filler)
        self.__button2 = Button(self.__mainwindow,background="azure4",command=self.button2_pressed,image=self.__filler)
        self.__button3 = Button(self.__mainwindow,background="azure4",command=self.button3_pressed,image=self.__filler)
        self.__button4 = Button(self.__mainwindow,background="azure4",command=self.button4_pressed,image=self.__filler)



        self.__timer = Label(text="0",background="white",font=("Fixedsys",16),bg="azure4")

        self.__mainwindow.grid_columnconfigure(0,weight=1)
        self.__mainwindow.grid_columnconfigure(1, weight=1)
        self.__mainwindow.grid_columnconfigure(2, weight=1)
        self.__mainwindow.grid_columnconfigure(3, weight=1)

        self.__mainwindow.grid_rowconfigure(0,weight = 1)
        self.__mainwindow.grid_rowconfigure(1, weight=1)
        self.__mainwindow.grid_rowconfigure(2, weight=1)
        self.__mainwindow.grid_rowconfigure(3, weight=1)

        self.__timer.grid(column=0,row=0,columnspan=4,sticky="EW")
        self.__button1.grid(column=0,row=1,sticky="NSEW")
        self.__button2.grid(column=1,row=1,sticky="NSEW")
        self.__button3.grid(column=2,row=1,sticky="NSEW")
        self.__button4.grid(column=3,row=1,sticky="NSEW")

        self.timer_thread = threading.Thread(target=self.timer)
        self.timer_thread.start()

        self.__timer_event = threading.Event()


        self.tiles_thread = threading.Thread(target=self.tiles)
        self.tiles_thread.start()

        self.__button_event1 = threading.Event()
        self.__button_event2 = threading.Event()
        self.__button_event3 = threading.Event()
        self.__button_event4 = threading.Event()

    def button1_pressed(self):

        self.__button_event1.set()
        self.__button1.configure(image=self.__filler)

    def button2_pressed(self):

        self.__button_event2.set()
        self.__button2.configure(image=self.__filler)

    def button3_pressed(self):

        self.__button_event3.set()
        self.__button3.configure(image=self.__filler)

    def button4_pressed(self):

        self.__button_event4.set()
        self.__button4.configure(image=self.__filler)


    def tiles(self):

        iteration = 0
        speed = 2

        while True:
            if iteration / 5 == 1:
                speed = speed/1.5
                iteration = 0

            num = random.randint(1, 4)
            self.__statetile1 = False
            self.__statetile2 = False
            self.__statetile3 = False
            self.__statetile4 = False

            time.sleep(speed)
            if num == 1:
                self.__button1.configure(image=self.__tonttu)
                self.__statetile1 = True
            elif num == 2:
                self.__button2.configure(image=self.__tonttu)
                self.__statetile2 = True
            elif num == 3:
                self.__button3.configure(image=self.__tonttu)
                self.__statetile3 = True
            elif num == 4:
                self.__button4.configure(image=self.__tonttu)
                self.__statetile4 = True


            if self.__statetile1:
                time.sleep(1)
                self.__button1.configure(image=self.__filler)
                if not self.__button_event1.is_set():
                    self.stop_timer()
                    self.get_record()
                    self.build_menu()
                    break

            if self.__statetile2:
                time.sleep(1)
                self.__button2.configure(image=self.__filler)
                if not self.__button_event2.is_set():
                    self.stop_timer()
                    self.get_record()
                    self.build_menu()
                    break

            if self.__statetile3:
                time.sleep(1)
                self.__button3.configure(image=self.__filler)
                if not self.__button_event3.is_set():
                    self.stop_timer()
                    self.get_record()
                    self.build_menu()
                    break

            if self.__statetile4:
                time.sleep(1)
                self.__button4.configure(image=self.__filler)
                if not self.__button_event4.is_set():
                    self.stop_timer()
                    self.get_record()
                    self.build_menu()
                    break

            self.__button_event1.clear()
            self.__button_event2.clear()
            self.__button_event3.clear()
            self.__button_event4.clear()

            iteration += 1

    def get_record(self):

        self.__ennatykset.append([self.__playernamestr,self.__seconds])



    def timer(self):
        self.__seconds = 0

        while True:
            self.__timer.configure(text=self.__seconds)
            self.__seconds += 1
            time.sleep(1)
            if self.__timer_event.is_set():
                break

    def stop_timer(self):
        self.__timer_event.set()
        self.timer_thread.join(timeout=0.0001)




    def build_highscores(self):


        self.clear_the_screen()

        self.__ennatyksetlabel = Label(text="Ennätykset",font=("Fixedsys",16),bg="azure4")
        self.__takaisinbutton = Button(text="Takaisin",command = self.build_menu,font=("Fixedsys"))

        self.__takaisinbutton.pack(anchor="w",side="bottom")
        self.__ennatyksetlabel.pack(pady = 20)

        for record in self.__ennatykset:

            self.__recordlabel = Label(text=f"{record[0]}: {record[1]} Sekuntia",bg="azure4",fg="green",font=("Fixedsys",16))
            self.__recordlabel.pack()






    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()

    def stop(self):

        self.__mainwindow.destroy()

def main():
    ui = Userinterface()

    ui.start()




if __name__ == "__main__":
    main()
