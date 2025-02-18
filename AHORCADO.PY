import random

# Lista de palabras
palabras = ["python", "computadora", "teclado", "programacion", "ahorcado"]
palabra = random.choice(palabras)
letras_adivinadas = []
oportunidades = 6

print("\nBienvenido al juego del Ahorcado!")
print("Adivina la palabra:")

# Mostrar palabra con guiones
palabra_oculta = "_" * len(palabra)
print(palabra_oculta)

while oportunidades > 0:
    letra = input("\nIngresa una letra: ").lower()
    
    if len(letra) != 1:
        print("Por favor, ingresa solo una letra.")
    elif letra in letras_adivinadas:
        print("Ya has intentado con esa letra.")
    else:
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            print("¡Bien hecho! La letra está en la palabra.")
            palabra_temporal = ""
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_temporal += letra
                else:
                    palabra_temporal += palabra_oculta[i]
            palabra_oculta = palabra_temporal
        else:
            print("Lo siento, la letra no está en la palabra.")
            oportunidades -= 1
            print(f"Te quedan {oportunidades} oportunidades.")
    
    print(palabra_oculta)

