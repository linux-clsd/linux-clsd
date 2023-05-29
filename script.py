import re
import getpass
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def evaluar_seguridad_contrasena(contrasena):
    puntaje = 0

    # Comprueba la longitud de la contraseña
    if len(contrasena) >= 8:
        puntaje += 1

    # Comprueba si la contraseña contiene al menos una letra mayúscula
    if re.search(r'[A-Z]', contrasena):
        puntaje += 1

    # Comprueba si la contraseña contiene al menos una letra minúscula
    if re.search(r'[a-z]', contrasena):
        puntaje += 1

    # Comprueba si la contraseña contiene al menos un número
    if re.search(r'\d', contrasena):
        puntaje += 1

    # Comprueba si la contraseña contiene al menos un carácter especial
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        puntaje += 1

    # Retorna una descripción según el puntaje obtenido
    if puntaje == 1:
        sugerencias = []
        if len(contrasena) < 8:
            sugerencias.append(f"Incrementar la longitud de la contraseña (actual: {len(contrasena)} caracteres).")
        if not re.search(r'[A-Z]', contrasena):
            sugerencias.append("Incluir al menos una letra mayúscula.")
        if not re.search(r'[a-z]', contrasena):
            sugerencias.append("Incluir al menos una letra minúscula.")
        if not re.search(r'\d', contrasena):
            sugerencias.append("Incluir al menos un número.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
            sugerencias.append("Incluir al menos un carácter especial.")

        mensaje = f"{Fore.RED}La contraseña es débil. ¡Peligro!\nRecomendaciones para mejorar la contraseña:"
        for sugerencia in sugerencias:
            mensaje += f"\n- {sugerencia}"

        return mensaje
    elif puntaje == 2:
        return f"{Fore.YELLOW}La contraseña es moderada. ¡Advertencia!"
    elif puntaje == 3:
        return f"{Fore.YELLOW}La contraseña es segura."
    elif puntaje == 4:
        return f"{Fore.GREEN}La contraseña es muy segura."
    elif puntaje == 5:
        return f"{Fore.GREEN}La contraseña es extremadamente segura."
    else:
        return f"{Fore.RED}La contraseña no cumple con los requisitos mínimos. ¡Peligro!"

# Solicitar al usuario que ingrese una contraseña sin mostrarla en pantalla
contrasena = getpass.getpass("Ingresa tu contraseña (no se mostrará en pantalla): ")

# Mostrar mensaje de confirmación
print("Has ingresado tu contraseña de forma segura.")

# Evaluar y mostrar la seguridad de la contraseña con colores, señales de peligro y recomendaciones
resultado = evaluar_seguridad_contrasena(contrasena)
print(resultado)
