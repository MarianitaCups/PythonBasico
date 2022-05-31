calificacion = input("Dame tu calificacios de la AZ-900: ")
calificacion = int(calificacion)

if calificacion < 700 : 
    print("No estudiaste")
elif calificacion > 1000 :
    print("No puedes sacar mas de 1000")
else :
    print("Yei, ve por tu certificado")
    
print("\n\n")   
edad = input("Dame tu edad: ")
edad = int(edad)

if edad >= 18 or edad <= 10 :
    print("Ya eres mayor de edad")
elif edad > 100 :
    print("si vienes con tus abuelos, te podemos fiar")
elif edad < 0 :
    print("No existes")
else :
    print("Eres menor de edad")