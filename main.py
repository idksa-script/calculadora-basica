import tkinter as tk 
from logicaCalculadora import borrar, agregar, calcular
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

#tamaño de los botones
ancho = 8
largo = 3
######################

#primer frame, caja o div donde se encuentran dos frame uno para la entrada y resultado de las operaciones y otro de botones 
frame_padre = tk.Frame(ventana, bg="black")
frame_padre.pack(fill="both", expand=True)

#frame hijo1 donde esta la entrada de texto
frame_hijo1 = tk.Frame(frame_padre, bg="black")
frame_hijo1.place(relx=0, rely=0, relwidth=1.0, relheight=0.35)
cuadro_texto = tk.Entry(frame_hijo1, font=("Monospace", 20), justify="right", validate="key", validatecommand=(validacion, "%P"), bg="black", fg="white", bd=0, highlightthickness=0)
cuadro_texto.pack(fill="both", expand=True)

############
#los botones se guardaran en una lista para hacerlas dentro de un for 
botones = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("C", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

#frame hijo2 donde estan los botones para ingresar el texto o mejor dicho las operaciones 
frame_hijo2 = tk.Frame(frame_padre, bg="black")
frame_hijo2.place(relx=0, rely=0.35, relwidth=1.0, relheight=0.65)

for i in range(4):
    frame_hijo2.rowconfigure(i, weight=1)
    frame_hijo2.columnconfigure(i, weight=1)

for texto, filas, columnas in botones:
    if texto == "C":
        boton = tk.Button(frame_hijo2, text=texto, command=lambda: borrar(cuadro_texto))

    elif texto == "=":
        boton = tk.Button(frame_hijo2, text=texto, command=lambda: calcular(cuadro_texto))

    else:
        boton = tk.Button(frame_hijo2, text=texto, command= lambda t= texto: agregar(cuadro_texto, t))
    boton.grid(row=filas, column=columnas, sticky="nsew")


ventana.mainloop()
