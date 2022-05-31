#string - palabras
nombre = "Mariana"

#enteros - numeros sin punto decimal
edad = 20
edad2 = "20"

print("Sin comillas")
print(edad + edad)

print("\nCon comillas")
print(edad2 + edad2)

#flotante - numeros con punto decimal
pi = 3.1416

print("\nCambiando de entero a float")
edad = float(edad) #cesteo - transformar un tipo de variable a otro
print(edad)

print("\n")
#para saber que tipo de varieble es tu variable
print(type (nombre), type (edad))   

print("\n")
#Bool - Booleano - si o no
legustas = False
legustas = True
print(legustas)