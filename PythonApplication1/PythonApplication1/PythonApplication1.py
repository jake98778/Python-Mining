#imports da shit
import tkinter as tk
import tkinter.font as tkFont

#also import os for cmd commands
import os
import sys

#import for threading
import threading

#Here is where Veribles are defined



#switch off is 0. Switch on is 1
switch = 0




def miner_start():
        os.system("setx GPU_FORCE_64BIT_PTR 0")
        os.system("setx GPU_MAX_HEAP_SIZE 100")
        os.system("setx GPU_USE_SYNC_OBJECTS 1")
        os.system("setx GPU_MAX_ALLOC_PERCENT 100")
        os.system("setx GPU_SINGLE_ALLOC_PERCENT 100")

        #need to edit below to be the work name. For now this works for tetsing
        os.system("ethminer -P stratum1+tcp://0xE3A8103F0c2E17E1AD0bc6935b1D35FB38470C82.deployment@naw-eth.hiveon.net:4444 --report-hashrate")

#sets switch to 0 to start program which is miner off
#removed for now. 
class App:
    def __init__(self, root):
        #setting title
        root.title("Crypto Miner v0.1")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        #starting to mess with switch stuff
        if (switch == 1):
            switch_text = "On"
        if (switch == 0):
            switch_text = "off"


        #creating buttons and UI content

        GButton_245=tk.Button(root)
        GButton_245["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "Start"
        GButton_245.place(x=280,y=30,width=70,height=25)
        GButton_245["command"] = self.GButton_245_command

        GButton_990=tk.Button(root)
        GButton_990["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_990["font"] = ft
        GButton_990["fg"] = "#000000"
        GButton_990["justify"] = "center"
        GButton_990["text"] = "Stop"
        GButton_990.place(x=280,y=70,width=70,height=25)
        GButton_990["command"] = self.GButton_990_command

        # Program is Running Text
        text = tk.StringVar()
        text.set("Test")
        label = tk.Label(root, textvariable=self.text)
        label.pack()

        GMessage_683=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_683["font"] = ft
        GMessage_683["fg"] = "#333333"
        GMessage_683["justify"] = "center"
        GMessage_683["text"] = "Note: Make sure to stop this program when playing games"
        GMessage_683.place(x=230,y=120,width=176,height=64)

    def GButton_245_command(self):
        print("Start button pressed")
        #add code here

        #changes switch value to 1
        switch = 1
        print(switch_text)
        #start thread for miner to run in
        thread = threading.Thread(target=miner_start, args=[])
        thread.start()
        print("thread started yay")

    def GButton_990_command(self):
        print("stop button pressed")
        #edit switch value
        switch = 0
        print(switch_text)
        #add code here
        os.system("TASKKILL /F /IM cmd.exe /T")
        #OMG IT WORKS. Probably closes all kinds of shit but it works so who cares. 

        #not working at the moment. Need to look into stoping a thread more and go that route. It works to start though so yay
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()