archivo = open("C:/Users/User/Desktop/Maestria/Herramientas para la IA/ejercicio-001-SantyPaul19/informacion.txt", "r")

lineas = archivo.readlines()
#print(lineas)

print("-------------------")

lineas = [r.split(";") for r in lineas ]

#print(lineas)


print("-------------------")

#for l in lineas:
    #print(l)


print("-------------------")
lineas = lineas[1:]
#for l in lineas:
    #apellido = l[1]
    #if apellido [0] == "B":
    #    print(l)


print("-------------------")
lineas = lineas[1:]
for l in lineas:
    correo = "org" in l[3]
    if correo == True:
        print(l)