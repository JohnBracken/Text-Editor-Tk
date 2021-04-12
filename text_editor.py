from tkinter import *
from tkinter import filedialog
import tkinter.font as font

window = Tk()
window.title("JSON File Reader")
window.geometry('1200x480')

myFont = font.Font(family="Montserrat", size=16, weight="bold")
#Set window size
frame1 = Frame(window, width=600, height=480, bg='azure')
frame2 = Frame(window, width=600, height=480, bg='mint cream')

frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)

label1 = Label(frame1,text='Files List',bg='azure')
label1['font'] = myFont
label1.place(x=20,y=20)

label2 = Label(frame2,text='File Text', bg='mint cream')
label2['font'] = myFont
label2.place(x=20,y=20)

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/home/johnb/Documents/tk_gui", 
        title="Open JSON file", 
        filetypes=(("JSON Files", "*.json"),
                   ("Text Files", "*.txt"))
        )
    tf = open(tf)  
    data = tf.read()
    txtarea.delete(1.0,END)
    txtarea.insert(END, data)
    tf.close()

def saveFile():
    sv = filedialog.asksaveasfile(mode='w',
        initialdir="/home/johnb/Documents/tk_gui", 
        title="Save JSON file", 
        filetypes=(("JSON Files", "*.json"),
                   ("Text Files", "*.txt"))
        )
    text_for_save = str(txtarea.get(0.0,END))
    sv.write(text_for_save)
    sv.close()
        

txtarea = Text(frame2, width=50, height=20, bg="old lace", font="Helvetica", fg='blue')
txtarea.place(x=20, y=60)


bt = Button(
    frame1, 
    text="Open File", 
    command=openFile
    )
bt['font'] = myFont
bt.place(x=20,y=60)

btn_save = Button(frame1, 
text="Save File",
command=saveFile
)

btn_save['font'] = myFont
btn_save.place(x=20,y=120)

window.mainloop()

