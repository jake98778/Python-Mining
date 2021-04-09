import os
import threading
import pyglet
from tkinter import *
from tkinter import messagebox

#Importing Pixel Style Font
pyglet.font.add_file('8bit.TTF')


#Setting Up the UI
root = Tk()
root.title("Gamer Miner")
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)
root.geometry("800x500")

##############################################################

#Background Picture
bg = PhotoImage(file="BG.png")

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
label = Label(root, textvariable=var, bg="#232027", fg="#ebe3f2", font='8bit.TTF')
var.set("Status: OFF")

#Text Entry Field
L1 = Label(root, text="Enter Your Name:", relief=FLAT, bg="#232027", fg="#ebe3f2")
L1.place(x=290, y=400)
E1 = Entry(root, bd=2, relief=FLAT, bg="#232027", fg="#ebe3f2", selectbackground="#ebe3f2", selectforeground="#232027")
E1.place(x=400, y=400)

###################################################

#Functions


###Submit
def submit():
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
        var.set("Status: MINING")
        thread = threading.Thread(target=miner_start, args=[])
        thread.start()
        print("(+) Bot started mining...")
        messagebox.showinfo("", "If you are getting a pop-up message from Windows Defender, please allow this program so that you can start mining.")


def onButtonEnter(e):
    onButton['background'] = 'black'


def onButtonLeave(e):
    onButton['background'] = 'grey'


###Turning the Miner Off
def turnOff():
    var.set("Status: OFF")
    os.system("TASKKILL /F /IM cmd.exe /T")
    print("(-) Bot has stopped mining.")


def offButtonEnter(e):
    offButton['background'] = 'black'


def offButtonLeave(e):
    offButton['background'] = 'grey'


onButton = Button(root, image=onButtonImg, command=turnOn, highlightthickness=0, bd=0)
offButton = Button(root, image=offButtonImg, command=turnOff, highlightthickness=0, bd=0)
submitButton = Button(root, text="SUBMIT", command=submit)

onButton.bind("<Enter>", onButtonEnter)
onButton.bind("<Leave>", onButtonLeave)

offButton.bind("<Enter>", offButtonEnter)
offButton.bind("<Leave>", offButtonLeave)


################################################################
#Placing the UI Elements
onButton.place(x=200, y=200)
offButton.place(x=425, y=200)
label.place(relx=.5, y=175, anchor="center")
submitButton.place(relx=.5, y=460, anchor="center")

#Worker Name Text Display
workerNameLabel = Label(root, textvariable=workerName, bg="#232027", fg="#ebe3f2")
workerName.set("Miner Name: " + str(workerNameTxtFile.read()))
workerNameLabel.place(relx=.5, y=360, anchor="center")

root.mainloop()
