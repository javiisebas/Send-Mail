
# coding: utf-8

# In[30]:


import smtplib
import sys 
from getpass import getpass    
from email.mime.text import MIMEText
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter import font
 
#file = filedialog.askopenfilename()

window = Tk() 
window.title("Correo electrónico") 
window.geometry('500x475')


# -----------CAJAS-----------
col = [0,2,4,6,8,9,11]  # Cajas en blanco
for i in col:
    lbl = Label(window, text=" ") 
    lbl.grid(column=0, row=i)
    
texto_cajas = ["Desde","Contraseña","Para","Asunto"] # Cajas con contenido
numero_fila = 1
for texto in texto_cajas:
    lbl = Label(window, text="    " + texto + " :  ") 
    lbl.grid(column=1, row=numero_fila,sticky = E)
    numero_fila += 2
# ----------------------------
    
# Usuario
emisor = Entry(window,width=59) 
emisor.grid(column=2, row=1,sticky = W)


# Contraseña del usuario
password = Entry(window,width=59,show="*")
password.grid(column=2, row=3,sticky = W)


# Receptor del mensaje
receptor = Entry(window,width=59) 
receptor.grid(column=2, row=5,sticky = W)


# Asunto del mensaje
asunto = Entry(window,width=59) 
asunto.grid(column=2, row=7,sticky = W)


# Mensaje
lbl4 = Label(window, text="         Mensaje :") 
lbl4.place(x=47,y=195)
texto = scrolledtext.ScrolledText(window,width=51,height=11) 
texto.place(x=47,y=230)


# Distintos tipos de servidores
def BuscaServidor(correo):
    servidor = correo[correo.find("@")+1:][:correo[correo.find("@")+1:].find(".")]
    print(servidor)
    if servidor == "gmail" or servidor == "ucm":
        return "smtp.gmail.com"
    if servidor == "yahoo":
        return "mail.yahoo.com"
    if servidor == "hotmail" or servidor == "outlook":
        return "smtp.live.com"


# Enviado del mensaje
def clicked(): 
    global emisor,receptor,password,asunto
    try:
        mensaje = MIMEText(texto.get("1.0",END)) 
        mensaje['From']=emisor.get()
        mensaje['To']=receptor.get()
        mensaje['Subject']=asunto.get()
        
        serverSMTP = smtplib.SMTP(BuscaServidor(emisor.get()),587) 
        serverSMTP.ehlo() 
        serverSMTP.starttls() 
        serverSMTP.ehlo() 
        serverSMTP.login(emisor.get(),password.get()) 

        serverSMTP.sendmail(emisor.get(),receptor.get(),mensaje.as_string()) 
        serverSMTP.close()
        messagebox.showinfo('Información','Correo enviado')
        
        # Reseteamos la información del correo
        texto.delete("1.0",END)
        receptor.delete(0,END)
        asunto.delete(0,END)
        
    except:
        messagebox.showinfo('Información','Usuario o contraseña incorrectos')

btn = Button(window, text="ENVIAR", command=clicked, width=58, height=1, anchor="center")
btn.place(x=46,y=427)

class MsgBox(Toplevel):

    def __init__(self, title="Información", message="Hello World"):
        Toplevel.__init__(self)

        self.title(title)
        
        self.font = font.Font(size=11)
        self.label = Label(self, text=message, font = self.font)
        self.label['bg'] = 'white'
        self.label.pack(ipadx=50, ipady=10, fill='both', expand=True)

        self.button = Button(self, text="Cerrar")
        self.button['command'] = self.destroy
        self.button.pack(pady=10, padx=10, ipadx=20, side='left')

# --- functions ---

def about():
    mensaje = """
    La aplicación ha sido creada
    con el fin de poder enviar
    correos de forma rápida y ágil.
    
    Pudiendo utilizar la misma 
    aplicación para cualquier cuenta
    de correo de gmail, hotmail y yahoo
    """
    msg = MsgBox("Información", mensaje)


# Menú
def limpiar():
    texto.delete("1.0",END)
    receptor.delete(0,END)
    asunto.delete(0,END)
    emisor.delete(0,END)
    password.delete(0,END)
    
def salirAplicacion():
    decision = messagebox.askquestion("Salir","Deseas salir de la aplicación?")
    if decision == "yes":
        window.destroy()
        
def link():
    import webbrowser
    webbrowser.open("javiersebastianfernandez.com")
    
def contact():
    receptor.insert(0,"javi.sebas@hotmail.es")
    asunto.insert(0,"Mensaje de usuario de EnviaCorreo")
    

menubar = Menu(window)
# Parte file del menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Configuracion", menu=filemenu)
filemenu.add_command(label="Borrar", command=limpiar)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=salirAplicacion, accelerator="Ctrl+w")
# Añadimos parte de información
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Información", command=about)
helpmenu.add_command(label="Desarrollador", command=link)
helpmenu.add_command(label="Contactar", command=contact)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

window.config(menu=menubar)


window.mainloop() 

