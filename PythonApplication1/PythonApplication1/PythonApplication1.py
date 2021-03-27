#imports da shit
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

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

        GMessage_683=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_683["font"] = ft
        GMessage_683["fg"] = "#333333"
        GMessage_683["justify"] = "center"
        GMessage_683["text"] = "Note: Make sure to stop this program when playing games"
        GMessage_683.place(x=230,y=120,width=176,height=64)

    def GButton_245_command(self):
        print("Start")
        #add code here


    def GButton_990_command(self):
        print("Stop")
        #add code here

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
