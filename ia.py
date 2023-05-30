import speech_recognition as sr
import pyttsx3
from datetime import datetime
from gtts import gTTS
import pygame

# Inicializar el reconocimiento de voz y el sintetizador de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Ajustar la configuración del reconocimiento de voz
recognizer.energy_threshold = 3000
recognizer.dynamic_energy_adjustment_ratio = 1.5

# Configurar el sintetizador de voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Puedes cambiar el índice para seleccionar una voz diferente

def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Procesando...")
        text = recognizer.recognize_google(audio, language='es')
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error al procesar la solicitud: {e}")
        return ""

def speak(text):
    tts = gTTS(text, lang='es')
    tts.save('output.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()

def assistant():
    while True:
        command = listen()

        if 'salir' in command:
            print("Hasta luego.")
            speak("Hasta luego.")
            break

        if 'hora' in command:
            current_time = datetime.now().strftime("%H:%M")
            print(f"La hora actual es: {current_time}")
            speak(f"La hora actual es: {current_time}")
        else:
            print("Comando no reconocido.")
            speak("No entendí ese comando.")

if __name__ == "__main__":
    print("Iniciando asistente de voz...")
    speak("Hola, ¿en qué puedo ayudarte?")
    assistant()

# Updated to actual version -- v-1.1