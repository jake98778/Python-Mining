import os
import threading
from tkinter import *
from tkinter import messagebox
from playsound import playsound


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

#Setting Up the UI
root = Tk()
root.title("Crypto Miner (v0.1)   Coded By: Jake & Matt")
root.resizable(width=False, height=False)
root.geometry("500x300")

#Background Picture
bg = PhotoImage(file="bg.png")

# Show Background Image using Label
bgLabel = Label( root, image = bg)
bgLabel.place(x = -2, y = -2)

var = StringVar()
workerName = StringVar()
label = Label( root, textvariable=var)
var.set("Miner is turned off.")

#Text Entry Field
L1 = Label(root, text="Enter Your Name:")
L1.pack( side = LEFT)
E1 = Entry(root, bd =1)
E1.pack(side=LEFT)


#Submit
def submit():
    input = E1.get()
    workerName.set("Miner Name: " + str(input))
    print(">>Worker Name: " + str(input) + "")
    playsound('button.mp3')


#Turning the Miner On
def turnOn():
    var.set("Miner is running.")
    thread = threading.Thread(target=miner_start, args=[])
    thread.start()
    print("(+) Bot started mining...")
    playsound('button.mp3')
    messagebox.showinfo("", "If you are getting a pop-up message from Windows Defender, please allow this program so that you can start mining.")


onButton = Button(root, text ="TURN ON", command = turnOn)


#Turning the Miner Off
def turnOff():
    var.set("Miner has stopped.")
    os.system("TASKKILL /F /IM cmd.exe /T")
    print("(-) Bot has stopped mining.")
    playsound('button.mp3')


offButton = Button(root, text ="TURN OFF", command = turnOff)

#Submit Entry Field Text Button
submitButton = Button(root, text ="SUBMIT", command = submit)
submitButton.place(x=230, y=135)

################################################################
#Packing the UI Elements
onButton.place(x=100, y=40)
offButton.place(x=170, y=40)
label.place(x=100, y=10)

#Worker Name Text Display
workerNameLabel = Label( root, textvariable=workerName)
workerName.set("Miner Name:")
workerNameLabel.place(x=0, y=175)

root.mainloop()
