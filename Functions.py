
from email.message import EmailMessage
import smtplib

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font


def ServerSearcher(mail):
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

    print(subject.get())
    print(transmitter.get())
    print(receiver.get())
    print(text.get("1.0",END))

    msg = EmailMessage()
    msg['Subject'] = subject.get()
    msg['From'] = transmitter.get()
    msg['To'] = receiver.get()
    msg.add_alternative(text.get("1.0",END), subtype='html')

    for file in fileList:
        fp =  open(file, 'rb') 
        data = fp.read()
        maintype = file.split(".")[-1]
        filename = file.split("/")[-1]
        msg.add_attachment(data, maintype = maintype, subtype = 'pdf', filename = filename)

    mailServer = smtplib.SMTP(ServerSearcher(transmitter.get()),587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(transmitter.get(),password.get())

    mailServer.sendmail(transmitter.get(),receiver.get(), msg.as_string())
    mailServer.close() 

    messagebox.showinfo('Information','Email successfully sent')
    
    # Reseteamos la información del mail
    text.delete("1.0",END)
    receiver.delete(0,END)
    subject.delete(0,END)
        


# Clase para generarme un message
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

    file = filedialog.askopenfilename()
    if len(file) != 0:

        num_attached += 1
        fileList.append(file)

    btn_attached_list["text"] = "   {}   ".format(str(num_attached))
    

def showAttached():
    message = ""
    counter = 1
    if len(fileList) == 0:
        message = "No file attached"
    else:
        for file in fileList:
            message += ("\n"+str(counter)+".  "+file)
            counter += 1
        
    msg = MsgBox("Attached files", message)


def deleteAdj():
    global num_attached, fileList

    num_attached = 0
    fileList = []

    btn_attached_list["text"] = "   {}   ".format(str(num_attached))


def about():
    message = """
     The application  has been
     created in order  to send 
     emails quickly and  agile.
    
     Being  able  to  use  the 
     same application for  any 
     account of gmail, hotmail 
     and yahoo mail.
    """
    msg = MsgBox("Information", message)


# Limpia las cajas cuando es llamada
def clean():
    text.delete("1.0",END)
    receiver.delete(0,END)
    subject.delete(0,END)
    transmitter.delete(0,END)
    password.delete(0,END)
  
  
# Cierra la ventana cuando es llamada  
def exitApp():
    decision = messagebox.askquestion("Exit","Would you like to exit the application?")
    if decision == "yes":
        window.destroy()