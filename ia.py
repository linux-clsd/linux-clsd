import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Inicializar el reconocimiento de voz y el sintetizador de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Procesando...")
        text = recognizer.recognize_google(audio, language='es')
        return text
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error al procesar la solicitud: {e}")
        return ""

def speak(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    engine.say(text)
    engine.runAndWait()

def assistant():
    while True:
        command = listen().lower()

        if 'salir' in command:
            print("Hasta luego.")
            speak("Hasta luego.")
            break

        if 'hora' in command:
            current_time = datetime.now().strftime("%H:%M")
            print(f"La hora actual es: {current_time}")
            speak(f"La hora actual es: {current_time}")

        print("Comando no reconocido.")
        speak("No entendí ese comando.")

if __name__ == "__main__":
    print("Iniciando asistente de voz...")
    speak("Hola, ¿en qué puedo ayudarte?")
    assistant()
