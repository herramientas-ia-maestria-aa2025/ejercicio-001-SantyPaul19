archivo = open("informacion.txt")
# print("El archivo se puede leer => ", archivo.readable())
VF = archivo.readable()
if (VF == False):
    print("Archivo txt no se puede abrir");
else:
    print(archivo.read());

