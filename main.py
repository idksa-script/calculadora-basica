import tkinter as tk 

def validar_entrada(entrada):
    carateres = "1234567890.+-*/%"
    for i in entrada:
        if i not in carateres:
            return False
    return True


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x600")

validacion = ventana.register(validar_entrada)

frame_padre = tk.Frame(ventana, bg="black")
frame_padre.pack(fill="both", expand=True)

frame_hijo1 = tk.Frame(frame_padre, bg="black")
frame_hijo1.place(relx=0, rely=0, relwidth=1.0, relheight=0.35)
#frame_hijo1.pack(fill="both", expand=True, padx=20, pady=20)
cuadro_texto = tk.Entry(frame_hijo1, font=("Arial", 14), justify="right", validate="key", validatecommand=(validacion, "%P"), bg="black", fg="white")
cuadro_texto.pack(fill="both", expand=True)

frame_hijo2 = tk.Frame(frame_padre, bg="red")
frame_hijo2.place(relx=0, rely=0.35, relwidth=1.0, relheight=0.65)


ventana.mainloop()
