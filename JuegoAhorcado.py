import os
print("Bienvenido al Juego Ahorcado")
print("Deberás adivinar la palabra con solo 3 intentos")
palabra = "serpiente"
secreta=palabra
comparar=palabra 
vocales = int(0)
consonantes = int(0)
lstvocales = "a,e,i,o,u"
fallidos=int(0)
correctas=int(0)
longitud=len(palabra)
for i,caracter in enumerate(palabra):
        secreta=secreta.replace(caracter,"*")            
print(f"La palabra tiene {longitud} letras")
for caracter in palabra: 
    if caracter in lstvocales:
        vocales= vocales+1
    else: 
        consonantes=consonantes+1
print(f"La palabra contiene {vocales} vocales y {consonantes} consonantes")
os.system("pause")
while fallidos<3:
    letra=input("\nEscriba letra\n:)")
    if letra in palabra:
        os.system("cls")
        print("\nEs correcta")
        correctas = correctas+1
        for i,caracter in enumerate(palabra):
            if caracter==letra:
                 comparar=comparar.replace(caracter,"*")           
    else:
        print("\nEs incorrecta")
        fallidos = fallidos+1
    print(f"""--------MARCADOR-------- 
>CORRECTAS {correctas}
>INCORRECTAS {fallidos}""")
    for i,caracter in enumerate(palabra):
        if comparar[i]=="*":
             print(f"{palabra[i]}",end="")
        else:
             print(f"{secreta[i]}",end="")
    if comparar==secreta:
        print("\n¡¡¡Has ganado el juego!!!:)\n")
        break
if fallidos==3:
     print("\nHas perdido :(")