import gdax
import time
from tkinter import *
from threading import Thread
import time


class Data():

    def __init__(self):
        self.public_client = gdax.PublicClient()

    def get_tick(self):
        return self.public_client.get_product_ticker(product_id="ETH-USD")["price"]

class View(Frame):
   
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.create_window()


    def create_window(self):
        self.data = Data()
        self.price = DoubleVar()
        self.current = DoubleVar()
        self.final = DoubleVar()

        eth = Label(self.master, text="ETH-USD Last Price:")
        eth.pack()
        lel2 = Label(self.master, text="")
        lel2.pack()

        display = Label(self.master, textvariable=self.price)
        display.pack()

        lel = Label(self.master, text="Held Volume:")
        lel.pack()

        lel3 = Label(self.master, text="")
        lel3.pack()

        display_3 = Label(self.master, textvariable=self.final)
        display_3.pack()

        display2 = Entry(self.master, textvariable=self.current)       
        display2.pack()

        button = Button(self.master, text="Confirm", command=self.update_volume)
        button.pack()

        self.update_thread = Thread(target=self.update_price)
        self.update_thread.start()

    def update_price(self):
        while(1):
            self.price.set(self.data.get_tick())
            time.sleep(0.1)

    def update_volume(self):
        self.final.set(self.price.get() * self.current.get())



root = Tk()
root.geometry("200x200")
app = View(root)
root.mainloop()


