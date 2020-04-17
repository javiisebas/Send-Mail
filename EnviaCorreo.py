# Author: Javier Sebastian Fernandez
# Contact: javi.sebas@hotmail.es


# We import all the needed libraries
import sys 
from getpass import getpass    

from email.message import EmailMessage
import smtplib

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font



# We define the functions we will use afterwards in the script
def ServerSearcher(mail):
    # The function returns the name of the server of a certain direction
    direction = mail.split("@")[-1].split(".")[0]
    server = {"gmail":"smtp.gmail.com",
              "ucm":"smtp.gmail.com",
              "yahoo":"smtp.mail.yahoo.com",
              "hotmail":"smtp.live.com",
              "outlook":"smtp.live.com",
              "office365":"smtp.office365.com"}

    return server[direction]


# Enviado del message
def clicked(): 
    global transmitter, receiver, password, subject, fileList, text

    transmitter_text = transmitter.get()
    receiver_text = receiver.get()
    password_text = password.get()
    subject_text = subject.get()
    message_text = text.get("1.0",END)

    information_complete = False

    if transmitter_text:
        if receiver_text:
            if password_text:
                if message_text:
                    information_complete = True


    if information_complete:

        try:
            # The function conects with the smtp server of mails and sends the mail
            msg = EmailMessage() # Creates the message
            msg['Subject'] = subject_text  # Subject of the message
            msg['From'] = transmitter_text # Transmitter of the message
            msg['To'] = receiver_text      # Receiver of the message
            msg.add_alternative(message_text, subtype='html') # Text of the message

            # If the user has attached a file it will introduce it on the message
            for file in fileList:
                fp =  open(file, 'rb')  # We open the file
                data = fp.read()        # We read it
                maintype = file.split(".")[-1] # We get the type of the file
                filename = file.split("/")[-1] # We get the name of the file
                # Finally we attach the file with the type and the name
                msg.add_attachment(data, maintype = maintype, subtype = 'pdf', filename = filename)

            # We connect with the mail server and we establish a connection
            mailServer = smtplib.SMTP(ServerSearcher(transmitter_text),587)
            mailServer.ehlo()     # Protocol 1
            mailServer.starttls() # Protocol 2
            mailServer.ehlo()     # Protocol 3

            try:
                mailServer.login(transmitter_text, password_text) # We do the log in with the user information

                try:
                    # Finally we send the mail from the transmitter to the receiver with the message
                    mailServer.sendmail(transmitter_text, receiver_text, msg.as_string())  
                    mailServer.close() # We end the connection with ther mail server

                    # We sent a mail due to the process has finished correctly
                    messagebox.showinfo('Information','Email successfully sent')
                    
                    # We reset the value of the parameters
                    text.delete("1.0",END)
                    receiver.delete(0,END)
                    subject.delete(0,END)

                except Exception: # Unknown Error
                    messagebox.showinfo('Información', 'Something has failed')

            except Exception: # Log in Error
                messagebox.showinfo('Information', 'Login has failed. \nCheck your user mail and password')

        except Exception: # Connection Error
            messagebox.showinfo('Information', 'Connection has failed. \nCheck your internet connection')

    else: # Information that the user must fill 
        messagebox.showinfo('Information', 'You have forgotten to fill in \nall the required information')
        


# We generate a class that will help us to generate a message
class MsgBox(Toplevel):
    def __init__(self, title=" ", message=" "):
        Toplevel.__init__(self)

        self.title(title)
        
        self.font = font.Font(size=11)
        self.label = Label(self, text=message, font = self.font)
        self.label['bg'] = 'white'
        self.label.pack(ipadx=50, ipady=10, fill='both', expand=True)

        self.button = Button(self, text="Close")
        self.button['command'] = self.destroy
        self.button.pack(pady=10, padx=10, ipadx=20, side='left')



def newAttached():
    global num_attached, fileList

    # The function attach new files
    file = filedialog.askopenfilename() # Open the directories to pick a file

    if file not in fileList:
        if len(file) != 0: # In case the user has picked a file

            num_attached += 1     # We add it to the counter of attached files
            fileList.append(file) # We introduce the path of the file in the list

    else:
        messagebox.showinfo('Information', 'The file has already been attached')
    # Finally we change the number of the attached files in the window
    btn_attached_list["text"] = "   {}   ".format(str(num_attached))
    


def showAttached():
    global fileList

    # The function shows the files that has been already attached
    message = ""
    counter = 1
    if len(fileList) == 0: # In case there is no file attached
        message = "No file attached"
    else:
        for file in fileList: # We get all the paths from the list
            message += ("\n"+str(counter)+".  "+file) # We add it to the message
            counter += 1
        
    # Finally we use the class MsgBox to print the message
    msg = MsgBox("Attached files", message) 



def deleteAdj():
    global num_attached, fileList

    # The function deletes the last files that have been attached
    num_attached -= 1        # Takes off one to the counter
    fileList = fileList[:-1] # Takes off the last file from the list

    # Finally we change the number of the attached files in the window
    btn_attached_list["text"] = "   {}   ".format(str(num_attached))



def about():

    # The function gives information about how the application works
    message = """
     The application  has been
     created in order  to send 
     emails quickly and  agile.
    
     Being  able  to  use  the 
     same application for  any 
     account of gmail, hotmail 
     and yahoo mail.
    """
    # Finally we use the class MsgBox to print the message
    msg = MsgBox("Information", message)



def clean():

    # The function deletes all the information that the user has introduced
    text.delete("1.0",END)
    receiver.delete(0,END)
    subject.delete(0,END)
    transmitter.delete(0,END)
    password.delete(0,END)
  
  

def exitApp():

    # The function close the application
    decision = messagebox.askquestion("Exit","Would you like to exit the application?")
    if decision == "yes":
        window.destroy()




# At this point we can start defining the objets of the screen and the elements that will compose it

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
lbl_attach.place(x=180,y=404)
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
btn_attached_list.place(x=270,y=400)
btn_attached_list["text"] = "   {}   ".format(str(num_attached))

# Button to delete the attached files
btn_attach = Button(window,text="  Delete last file attached ", command=deleteAdj)
btn_attach.place(x=320,y=400)

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