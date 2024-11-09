""" Pide al usuario un numero. Muestra su tabla de multiplicar del 1 al 10 
utilizando el ciclo ‘for’."""


# numero=int(input("ingrese un numero: "))

# for i in range(1,11):
#     print(f"{numero} X {i} = {numero*i}")


"""Cree un bucle que sume los números del 100 al 200"""

# suma=0

# for contador in range(100,201):
#     suma=suma+contador

# print(suma)



# palabra="Hola"
# lista=[4,6,2,7,2,6,"a"]
# lista2=["a","b"]

# lista.append("Nicolas")
# lista.insert(1,"Nicolas")
# lista.extend(lista2)
# lista=lista+lista2

# letra=lista.remove("a")
# letra=lista.pop(1)

# print(len(lista))
# print(letra)


"""Meter los números del 1 al 35 en una lista y mostrarla en pantalla. 
Hacer lo mismo para un rango de números indicado por un usuario.
"""


# lista=[]

# for numero in range(1,36):
#     lista.append(numero)

# print(lista)

# limite_Inf=int(input("ingrese el limite inf: "))
# limite_Sup=int(input("ingrese el limite sup: "))

# lista=[]

# for numero in range(limite_Inf,limite_Sup+1):
#     lista.append(numero)

# print(lista)


"""Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios."""

# Palabra=input("Ingrese un mensaje: ")
# lista=[]

# for i in range(0,len(Palabra)):
#     if Palabra[i]!=" ":
#         lista.append(Palabra[i])

# print(lista)


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""


# lista=["Matemáticas","Física","Química"]
# print(lista)

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""


# lista=["Matemáticas","Física","Química"]
# for i in range(0,len(lista)):
#     print("yo estudio:",lista[i])


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
una de las correspondientes notas introducidas por el usuario."""


# lista=["Matemáticas","Física","Química"]
# listaNotas=[]

# for i in range(0,len(lista)):
#     nota=input(f"cual es su nota en {lista[i]}: ")
#     listaNotas.append(nota)

# for i in range(0,len(listaNotas)):
#     print("En "+lista[i]+", has sacado "+listaNotas[i])


"""Crea una tupla con números, pide un numero por teclado e indica cuantas 
veces se repite."""

# tupla=(1,2,3,4,3,7,8,57,60)
# numero=int(input("ingrese un numero: "))

# cont=0

# for i in range(0,len(tupla)):
#     if numero==tupla[i]:
#         cont=cont+1

# print(f"El numero {numero} se repite {cont}")

"""D"""



# lista=["a","e","i","o","u"]

# for i in range(0,len(lista)):
#     print(lista[i])

# for caracter in lista:
#     print(caracter)

# dicc={"Nicolas":7,"Pablo":9,"Nacho":4}
# dicc["Nacho"]=10
# print(dicc)

# for key in dicc:
#     print(f"la llave es {key}, y el valor es: {dicc[key]}")


"""Crea un programa que pida al usuario el nombre de un mes (Enero, Febrero, etc.) 
y diga cuántos días tiene (por ejemplo, 30. Para simplificarlo vamos a suponer que 
febrero tiene 28 días.
"""

# fechas={"enero":31,"febrero":28,"marzo":31}
# mes=input("ingrese un mes: ")
# print(fechas[mes])


"""Crear un programa que pida al usuario un nombre de un alumno, y luego muestre la 
lista de notas de ese alumno. Usar diccionarios
"""

# notas={"Nico":[1,2,3],"Pablo":[4,5,6],"Nacho":[7,8,9]}

# nombre=input("ingrese un nombre: ")


# if nombre in notas:
#     print(notas[nombre])

# else:
#     print("ese alumno no esta")



"""Escribir un programa que pregunte al usuario los números ganadores de la lotería, 
los almacene en una lista y los muestre por pantalla ordenados de menor a 
mayor."""

lista=[]

while True:
    numero=input("Ingrese el numero (Salir para salir): ")
    if numero=="salir":
        break

    numero=int(numero)
    lista.append(numero)


for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[j]<lista[i]:
            temp=lista[j]
            lista[j]=lista[i]
            lista[i]=temp


print(lista)









