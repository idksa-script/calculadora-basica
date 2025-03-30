def borrar(cuadro_texto):
    cuadro_texto.delete(0, "end")

def agregar(cuadro_texto, t):
    cuadro_texto.insert("end", t)

def calcular(cuadro_texto):
    resultado = eval(cuadro_texto.get())
    cuadro_texto.delete(0, "end")
    cuadro_texto.insert("end", resultado)
