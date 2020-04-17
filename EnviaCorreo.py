# Author: Javier Sebastian Fernandez
# Contact: javi.sebas@hotmail.es


# We import all the needed libraries
import sys 
from getpass import getpass    

from Functions import *


# We create de main window
window = Tk() 
window.title("Mail Sender") 
window.geometry('500x500')


# -----------------Labels-----------------
# Boxes with no label
col = [0,2,4,6,8,9,11]  
for i in col:
    lbl = Label(window, text=" ") 
    lbl.grid(column=0, row=i)
   
# Box labels  
label_text = ["From","Password","To","Subject"] 
row = 1
for text in label_text:
    lbl = Label(window, text="    " + text + " :  ") 
    lbl.grid(column=1, row=row,sticky = E)
    row += 2

# Message box label
lbl_msg = Label(window, text="         Message :") 
lbl_msg.place(x=47,y=195)

# Attach new file label
lbl_attach = Label(window, text="Attached files: ")
lbl_attach.place(x=250,y=404)
# ----------------------------------------
    
# Mail of the user
transmitter = Entry(window,width=59) 
transmitter.grid(column=2, row=1,sticky = W)

# Password of the user
password = Entry(window,width=59,show="*")
password.grid(column=2, row=3,sticky = W)

# Mail of the receiver
receiver = Entry(window,width=59) 
receiver.grid(column=2, row=5,sticky = W)

# Subject of the message
subject = Entry(window,width=59) 
subject.grid(column=2, row=7,sticky = W)

# Message from the user
text = scrolledtext.ScrolledText(window,width=51,height=9) 
text.place(x=47,y=230)

# Variables to attach the files
fileList = []
num_attached = 0

# Button to attach new filws
btn_attach = Button(window,text="  Attach file  ", command=newAttached)
btn_attach.place(x=47,y=400)

# Button to see the attached files
btn_attached_list = Button(window,text=str(num_attached), command=showAttached)
btn_attached_list.place(x=360,y=400)
btn_attached_list["text"] = "   {}   ".format(str(num_attached))

# Button to delete the attached files
btn_attach = Button(window,text="  Delete  ", command=deleteAdj)
btn_attach.place(x=405,y=400)

# Button to send the mail
btn = Button(window, text="SEND", command=clicked, width=58, height=1, anchor="center")
btn.place(x=46,y=447)
  

# We create the element menu
menubar = Menu(window)

# We create the section Configuration
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Delete", command=clean)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitApp)

# We add the section to the menu
menubar.add_cascade(label="Configuration", menu=filemenu)

# We create the section Configuration
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Information", command=about)

# We add the section to the menu
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

# Mainloop to maintain the window working
window.mainloop() 