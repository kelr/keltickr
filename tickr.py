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
        self.price = IntVar()
        self.current = IntVar()

        display = Message(self.master, textvariable=self.price)
        display.grid(row=2, column=1)
        display.pack()

        display_3 = Message(self.master, textvariable=self.current*self.price)
        display_3.pack()

        display2 = Entry(self.master, textvariable=self.current)       
        display2.pack()

        self.update_thread = Thread(target=self.update_price)
        self.update_thread.start()

    def update_price(self):
        while(1):
            self.price.set(self.data.get_tick())
            time.sleep(0.1)


root = Tk()
app = View(root)
root.mainloop()


