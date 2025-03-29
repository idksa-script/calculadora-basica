def borrar(cuadro_texto):
    cuadro_texto.delete(0, "end")

def agregar(cuadro_texto, t):
    cuadro_texto.insert("end", t)
