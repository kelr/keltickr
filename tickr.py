import gdax
import time
from Tkinter import *
from threading import Thread


class View(Frame):
   
   def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.data = Data()

        l = Label(self.master, textvariable = gdax)
        l.pack()

root = Tk()
app = View(root)
root.mainloop()

class Data():

    def __init__(self):
        self.public_client = gdax.PublicClient()

    def get_tick(self):
        return self.public_client.get_product_ticker(product_id="ETH-USD")["price"]
