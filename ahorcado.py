import random

def elegir_palabra():
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "computadora"]
    return random.choice(palabras)

def jugar():
    palabra = elegir_palabra()
    palabra_guiones = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0 and "_" in palabra_guiones:
        print("Palabra: " + " ".join(palabra_guiones))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        
        letra = input("Introduce una letra: ").lower()

        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue
