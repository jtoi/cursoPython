import tkinter as tk
from tkinter import messagebox

from ejercicio25 import GestorPersonas as GP

def buscar():
    print("Buscando...")
    persona_buscada = campo_entrada.get()
    gp = GP()
    try:
        email = gp.get_email(persona_buscada)
        messagebox.showinfo ("Email: " , email)
    except KeyError:
        messagebox.showerror ("KO", "No se pudo encontrar el usuario")


if __name__ == '__main__':
    # Paso 1: La ventana
    ventana = tk.Tk()
    ventana.title('Busca Emails v1.0')
    ventana.geometry("250x130+300+100")
    # Paso 2: Etiqueta
    etiqueta = tk.Label(text='Nombre: ')
    etiqueta.place(x=30, y=30)
    # Paso 3: Campo de Texto
    campo_entrada = tk.Entry()
    campo_entrada.place(x=90,y=30)
    # paso 4: Botón
    boton = tk.Button(text='Buscar',command=buscar)
    boton.place(x=110,y=80)


    ventana.mainloop()