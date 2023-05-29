import subprocess
import sys

def scan_vulnerabilities():
    try:
        subprocess.run(["openvas", "scan", "-oX", "vulnerabilities_report.xml"])
        print("Escaneo de vulnerabilidades completado. Se generó un informe en vulnerabilities_report.xml.")
    except FileNotFoundError:
        print("El comando 'openvas' no se encontró en el sistema. Asegúrate de tenerlo instalado.")

def exit_program():
    print("Gracias por utilizar el programa de mejora de seguridad para Linux. ¡Hasta luego!")
    sys.exit()

def main():
    print("Bienvenido al programa de mejora de seguridad para Linux")

    while True:
        print("\nSeleccione una opción:")
        print("1. Escanear vulnerabilidades")
        print("2. Salir")

        choice = input("Opción: ")

        if choice == "1":
            scan_vulnerabilities()
        elif choice == "2":
            exit_program()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
