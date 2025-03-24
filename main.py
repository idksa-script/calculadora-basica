import tkinter as tk 

#verifica la entrada del teclado asegurandose de que no sea letras solo numero y ciertos simnolos
def validar_entrada(entrada):
    carateres = "1234567890.+-*/%"
    for i in entrada:
        if i not in carateres:
            return False
    return True


#ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x600")

validacion = ventana.register(validar_entrada)

#primer frame, caja o div donde se encuentran dos frame uno para la entrada y resultado de las operaciones y otro de botones 
frame_padre = tk.Frame(ventana, bg="black")
frame_padre.pack(fill="both", expand=True)

#frame hijo1 donde esta la entrada de texto
frame_hijo1 = tk.Frame(frame_padre, bg="black")
frame_hijo1.place(relx=0, rely=0, relwidth=1.0, relheight=0.35)
cuadro_texto = tk.Entry(frame_hijo1, font=("Arial", 14), justify="right", validate="key", validatecommand=(validacion, "%P"), bg="black", fg="white", bd=0, highlightthickness=0)
cuadro_texto.pack(fill="both", expand=True)

#frame hijo2 donde estan los botones para ingresar el texto o mejor dicho las operaciones 
frame_hijo2 = tk.Frame(frame_padre, bg="black")
frame_hijo2.place(relx=0, rely=0.35, relwidth=1.0, relheight=0.65)
boton1 = tk.Button(frame_hijo2, text="hola mundo", width=5, height=3)
boton1.pack(pady=20)


ventana.mainloop()
