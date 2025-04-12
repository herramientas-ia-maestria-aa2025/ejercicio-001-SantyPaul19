archivo = open("C:/Users/User/Desktop/Maestria/Herramientas para la IA/ejercicio-001-SantyPaul19/informacion.txt", "r")
# print("El archivo se puede leer => ", archivo.readable())
VF = archivo.readable()
if (VF == False):
    print("Archivo txt no se puede abrir")
else:
    print(archivo.read())

