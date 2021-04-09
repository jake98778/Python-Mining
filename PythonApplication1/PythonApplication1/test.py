import os
import threading
from tkinter import *

status = 0


#CMD Commands
def miner_start():
    os.system("setx GPU_FORCE_64BIT_PTR 0")
    os.system("setx GPU_MAX_HEAP_SIZE 100")
    os.system("setx GPU_USE_SYNC_OBJECTS 1")
    os.system("setx GPU_MAX_ALLOC_PERCENT 100")
    os.system("setx GPU_SINGLE_ALLOC_PERCENT 100")

    # need to edit below to be the work name. For now this works for testing
    os.system(
        "ethminer -P stratum1+tcp://0xE3A8103F0c2E17E1AD0bc6935b1D35FB38470C82.deployment@naw-eth.hiveon.net:4444 --report-hashrate")


root = Tk()
root.title("Crypto Miner (v0.1)")
root.resizable(width=False, height=False)
root.geometry("450x300")
var = StringVar()
label = Label( root, textvariable=var)
var.set("Program is turned off.")


#Turning the Button On
def turnOn():
    var.set("Program is running.")
    thread = threading.Thread(target=miner_start, args=[])
    thread.start()
    print("Bot started mining...")

onButton = Button(root, text ="TURN ON", command = turnOn)

#Turning the Button Off
def turnOff():
    var.set("Program is stopped.")
    os.system("TASKKILL /F /IM cmd.exe /T")
    print("Bot has stopped mining.")


offButton = Button(root, text ="TURN OFF", command = turnOff)

onButton.pack()
offButton.pack()
label.pack()
root.mainloop()