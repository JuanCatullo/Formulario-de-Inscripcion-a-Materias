
import tkinter
import tkinter.messagebox


ventana = tkinter.Tk()
ventana.title("")
ventana.geometry("500x500")
ventana.resizable(0,0)

cabecera = tkinter.Label(ventana, text= "   BIENVENIDO AL FORMULARIO   ").pack()


def saludo():
    tkinter.Label(ventana, text="Matematica").pack()

def salir():
    ventana.destroy()

boton = tkinter.Button(ventana, text="SELECCIONAR MATERIAS A RENDIR", command= saludo, fg= "black")
boton.pack()
boton.place(x=90, y=50, height=65, width=350)

boton2 = tkinter.Button(ventana, text="SALIR DEL FORMULARIO", command = salir, fg= "black")
boton2.pack()
boton2.place(x=90, y=400, height=65, width=300)

tkinter.messagebox.showinfo("","LE RECORDAMOS QUE SOLO HABRA UNA FECHA PARA SU INSCRIPCION")







ventana.mainloop()