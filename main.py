opcion=input("1_ Nombre completo, 2_Calculadora ")

if opcion=="1":
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    print("Su nombre completo es: ",nombre,apellido)
elif opcion=="2":
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    suma=num1+num2
    resta=num1-num2
    multiplicacion=num1*num2
    division=num1/num2
    print("La suma es: ",suma)
    print("La resta es: ",resta)
    print("La multiplicacion es: ",multiplicacion)
    print("La division es: ",division)
else:
    print("Opcion no valida")   
