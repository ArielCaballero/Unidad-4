from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana=None
    __altura=None
    __peso=None
    __IMC=None
    __estado=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x250')
        self.__ventana.title('Calculadora de IMC')
        Label(text="Calculadora de IMC", font=("Arial", 14), bg="gray").pack(side=TOP, fill=BOTH, expand=True)
        frame1 = Frame(self.__ventana)
        frame1.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame2 = Frame(self.__ventana)
        frame2.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame3 = Frame(self.__ventana)
        frame3.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame4 = Frame(self.__ventana)
        frame4.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__IMC = StringVar()
        self.__estado = StringVar()
        Label(frame1, text="Altura:").pack(side=LEFT, fill=BOTH, expand=True)
        self.alturaEntry = ttk.Entry(frame1, textvariable=self.__altura)
        self.alturaEntry.pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame2, text="Peso:").pack(side=LEFT, fill=BOTH, expand=True)
        self.pesoEntry = ttk.Entry(frame2, textvariable=self.__peso)
        self.pesoEntry.pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Button(frame3, text="Calcular", bg="green", relief='flat', fg='white',command=self.calcular).pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        Button(frame3, text="Limpiar", bg="green", relief='flat', fg='white',command=self.limpiar).pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame4, text="Tu indice de Masa Corporal (IMC) es: ").pack(side=LEFT, fill=BOTH, expand=True)
        Label(frame4, textvariable=self.__IMC).pack(side=RIGHT, fill=BOTH, expand=True)
        Label(self.__ventana, textvariable=self.__estado).pack(side=BOTTOM, fill=BOTH, expand=True,padx=5, pady=5)
        for child in self.__ventana.winfo_children():
            self.__ventana.mainloop()
    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__IMC.set('')
        self.__estado.set('')
        self.alturaEntry.focus()
    def calcular(self, *args):
        if self.alturaEntry.get()!='' and self.pesoEntry.get()!='':
            try:
                valor1=float(self.alturaEntry.get())/100    
                valor2=float(self.pesoEntry.get())
                resultado=valor2/(valor1*valor1)
                self.__IMC.set(resultado)
                if resultado<18.5:
                    self.__estado.set("Peso inferior al Normal")
                elif resultado<25:
                    self.__estado.set("Peso Normal")
                elif resultado<30:
                    self.__estado.set("Peso superior al Normal")
                else:
                    self.__estado.set("Obesidad")
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        else:
            self.__IMC.set('')