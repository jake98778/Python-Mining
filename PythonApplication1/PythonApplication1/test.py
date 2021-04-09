import os
import threading
from tkinter import *
from tkinter import messagebox
from playsound import playsound


#Setting Up the UI
root = Tk()
root.title("Gamer Miner")
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)
root.geometry("800x500")

##############################################################

#Background Picture
bg = PhotoImage(file="bg.png")

# Show Background Image using Label
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

#Variables
global nameEntry
var = StringVar()
workerName = StringVar()
workerNameTxtFile = open("workerName.txt", "r+")

#Button Images
offButtonImg = PhotoImage(file=r"offButton.png")
onButtonImg = PhotoImage(file=r"onButton.png")

#Miner Status Label
label = Label( root, textvariable=var)
var.set("Miner is turned off.")

#Text Entry Field
L1 = Label(root, text="Enter Your Name:")
L1.place(x=290, y=350)
E1 = Entry(root, bd=2)
E1.place(x=400, y=350)

###################################################

#Functions


###Submit
def submit():
    playsound('button.mp3')
    global nameEntry
    nameEntry = E1.get()
    #Check if they have not entered a worker name
    if nameEntry == "":
        print("User has not entered a worker name.")
        messagebox.showinfo("Gamer Miner", "Please enter a miner name so you can receive payouts.")
    else:
        workerNameTxtFile.write(nameEntry)
        workerName.set("Miner Name: " + nameEntry)
        print(">>Worker Name: " + nameEntry)


###CMD Commands
def miner_start():
    global nameEntry
    nameEntry = E1.get()
    os.system("setx GPU_FORCE_64BIT_PTR 0")
    os.system("setx GPU_MAX_HEAP_SIZE 100")
    os.system("setx GPU_USE_SYNC_OBJECTS 1")
    os.system("setx GPU_MAX_ALLOC_PERCENT 100")
    os.system("setx GPU_SINGLE_ALLOC_PERCENT 100")

    # need to edit below to be the work name. For now this works for testing
    os.system(
        "ethminer -P stratum1+tcp://0xE3A8103F0c2E17E1AD0bc6935b1D35FB38470C82." + nameEntry + "@naw-eth.hiveon.net:4444 --report-hashrate")


###Turning the Miner On
def turnOn():
    global nameEntry
    nameEntry = E1.get()
    # Check if they have not entered a worker name
    if nameEntry == "":
        print("User has not entered a worker name.")
        messagebox.showinfo("Gamer Miner", "Please enter a miner name so you can receive payouts.")
    else:
        var.set("Miner is running.")
        thread = threading.Thread(target=miner_start, args=[])
        thread.start()
        print("(+) Bot started mining...")
        playsound('button.mp3')
        messagebox.showinfo("", "If you are getting a pop-up message from Windows Defender, please allow this program so that you can start mining.")


###Turning the Miner Off
def turnOff():
    var.set("Miner has stopped.")
    os.system("TASKKILL /F /IM cmd.exe /T")
    print("(-) Bot has stopped mining.")
    playsound('button.mp3')


onButton = Button(root, image=onButtonImg, command=turnOn, highlightthickness=0, bd=0)
offButton = Button(root, image=offButtonImg, command=turnOff, highlightthickness=0, bd=0)
submitButton = Button(root, text="SUBMIT", command=submit)

################################################################
#Placing the UI Elements
onButton.place(x=200, y=200)
offButton.place(x=425, y=200)
label.place(relx=.5, y=175, anchor="center")
submitButton.place(relx=.5, y=430, anchor="center")

#Worker Name Text Display
workerNameLabel = Label( root, textvariable=workerName)
workerName.set("Miner Name: " + str(workerNameTxtFile.read()))
workerNameLabel.place(relx=.5, y=470, anchor="center")

root.mainloop()
