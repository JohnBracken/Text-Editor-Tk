#Text editor created using Python Tkinter module.

#Load tkinter libraries.  Need filedialog widget
#to open and save files.
from tkinter import *
from tkinter import filedialog
import tkinter.font as font

#Create text editor window.  Set size and title.
window = Tk()
window.title("JSON File Reader")
window.geometry('1200x480')

#Set main font for text editor window.
myFont = font.Font(family="Montserrat", size=16, weight="bold")

#Set window frame size and color for each of two frames.
frame1 = Frame(window, width=600, height=480, bg='azure')
frame2 = Frame(window, width=600, height=480, bg='mint cream')

#Place both frames on the text editor window.
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)

#Create files list label.
label1 = Label(frame1,text='Files List',bg='azure')
label1['font'] = myFont
label1.place(x=20,y=20)

#Create Text file text display label.
label2 = Label(frame2,text='File Text', bg='mint cream')
label2['font'] = myFont
label2.place(x=20,y=20)

#Define a function to open a text file.
#Give the option to open either JSON or plain text files.
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="~/Documents/tk_gui", 
        title="Open JSON file", 
        filetypes=(("JSON Files", "*.json"),
                   ("Text Files", "*.txt"))
        )
    tf = open(tf)  #Open and read the file.  
    data = tf.read()

    #Delete text display of previous file data if present.
    #Only want to show one file at a time.
    txtarea.delete(1.0,END)

    #Insert new text data and close the file.
    txtarea.insert(END, data)
    tf.close()

#Function to save text displayed to a text file
#either JSON or plain text.
def saveFile():
    sv = filedialog.asksaveasfile(mode='w',
        initialdir="~/Documents/tk_gui", 
        title="Save JSON file", 
        filetypes=(("JSON Files", "*.json"),
                   ("Text Files", "*.txt"))
        )
    #Convert text displayed into a single string
    text_for_save = str(txtarea.get(0.0,END))

    #Write to file and close file.
    sv.write(text_for_save)
    sv.close()
        
#Set text area display size, background color, font text and color..
txtarea = Text(frame2, width=50, height=20, bg="old lace", font="Helvetica", fg='blue')

#Place text area on specific location on the frame in the window.
txtarea.place(x=20, y=60)

#Create an open file button to run the open file function when pressed
bt = Button(
    frame1, 
    text="Open File", 
    command=openFile
    )
bt['font'] = myFont
bt.place(x=20,y=60)

#Create a save file button to save the currently displayed text to a file
#when pressed.
btn_save = Button(frame1, 
text="Save File",
command=saveFile
)

btn_save['font'] = myFont
btn_save.place(x=20,y=120)

#Main loop to keep text editor window open and running.
window.mainloop()

