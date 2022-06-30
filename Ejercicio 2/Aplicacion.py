from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana=None
    __preciobase=None
    __porcentaje=None
    __IVA=None
    __Total=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x350')
        self.__ventana.title('Calculadora de IMC')
        Label(text="Calculadora de IMC", font=("Arial", 14), bg="#00aae4").pack(side=TOP, fill=BOTH, expand=True)
        frame1 = Frame(self.__ventana)
        frame1.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame2 = Frame(self.__ventana)
        frame2.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame3 = Frame(self.__ventana)
        frame3.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame4 = Frame(self.__ventana)
        frame4.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame5 = Frame(self.__ventana)
        frame5.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        self.__precio = StringVar()
        self.__porcentaje = StringVar()
        self.__IVA = StringVar()
        self.__Total = StringVar()
        Label(frame1, text="Precio Base:").pack(side=LEFT, fill=BOTH, expand=True)
        self.precioEntry = Entry(frame1, textvariable=self.__precio)
        self.precioEntry.pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Radiobutton(frame2, text="IVA 21%", variable=self.__porcentaje, value=21).pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        Radiobutton(frame2, text="IVA 10.5%", variable=self.__porcentaje, value=10.5).pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame3, text="IVA").pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        self.IVAEntry = Entry(frame3, textvariable=self.__IVA, justify="center", state="disabled")
        self.IVAEntry.pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame4, text="Total").pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        self.TotalEntry = Entry(frame4, textvariable=self.__Total, justify="center", state="disabled")
        self.TotalEntry.pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Button(frame5, text="Calcular", bg="green", font=("Arial", 14), relief='flat',command=self.calcular).pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        Button(frame5, text="Salir", bg="red", font=("Arial", 14), relief='flat',command=self.salir).pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        self.__ventana.mainloop()
    def salir(self):
        self.__ventana.destroy()
    def calcular(self, *args):
        if self.precioEntry.get()!='' and self.__porcentaje!=None:
            try:
                valorbase=float(self.precioEntry.get())   
                porcentajeiva= float(self.__porcentaje.get())
                resultado=valorbase*porcentajeiva/100
                self.__IVA.set(resultado)
                self.__Total.set(float(self.precioEntry.get())+float(self.__IVA.get()))
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        else:
            self.__IVA.set('')
