import gdax
import time
from tkinter import *
from threading import Thread
import time


class Data():

    def __init__(self):
        self.public_client = gdax.PublicClient()

    def get_tick(self):
        print("hi")
        return self.public_client.get_product_ticker(product_id="ETH-USD")["price"]

class View(Frame):
   
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.create_window()


    def create_window(self):
        self.data = Data()
        self.price = StringVar()

        display = Message(self.master, textvariable=self.price)
        display.grid(row=2, column=1)
        display.pack()

        self.update_thread = Thread(target=self.update_price)
        self.update_thread.start()

    def update_price(self):
        while(1):
            self.price.set(self.data.get_tick())
            time.sleep(0.1)


root = Tk()
app = View(root)
root.mainloop()


