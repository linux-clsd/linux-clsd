# Linux CLSD 🤖

| [¿Qué es linux-clsd?](#¿qué-es-linux-clsd) | [Como usar l-clsd](#como-usar-l-clsd-ᵥ₋₁₁) | [Changelog](#changelog) |

------------------------------------------------------------------------------------------------------
![GitHub Repo stars](https://img.shields.io/github/stars/linux-clsd/linux-clsd?style=plastic) ![GitHub followers](https://img.shields.io/github/followers/linux-clsd?style=plastic) ![Uptime Robot status](https://img.shields.io/uptimerobot/status/m794441368-3749853622b1e76cd00e5292?style=plastic) ![Uptime Robot ratio (7 days)](https://img.shields.io/uptimerobot/ratio/7/m794441368-3749853622b1e76cd00e5292?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/linux-clsd/linux-clsd?style=plastic) ![Github-version](https://img.shields.io/badge/version-1.1-green?style=plastic)

## ¿Qué es Linux-CLSD?

El script es un asistente de voz básico llamado "Linux-CLSD" implementado en Python. Utiliza las bibliotecas SpeechRecognition, pyttsx3 y gTTS para realizar reconocimiento de voz, síntesis de voz y reproducción de audio.

"Linux-CLSD" permite al usuario interactuar con el asistente a través de comandos de voz. Al ejecutar el script, "Linux-CLSD" da la bienvenida y pregunta cómo puede ayudar.

El asistente espera a que el usuario hable y luego utiliza el reconocimiento de voz para convertir el audio en texto. A través del servicio de reconocimiento de voz de Google, el texto se analiza y se intenta determinar el comando o la acción solicitada por el usuario.

Si el comando es reconocido, "Linux-CLSD" realiza la acción correspondiente. Actualmente, el script admite dos comandos: "hora" y "salir". Si el usuario dice "hora", "Linux-CLSD" responde con la hora actual. Si el usuario dice "salir", "Linux-CLSD" se despide y el script termina.

Si el comando no es reconocido o no se entiende, "Linux-CLSD" indica que no comprendió el comando y espera a que el usuario hable nuevamente.

El asistente utiliza la síntesis de voz para convertir el texto en voz y reproducirlo a través de la salida de audio. Esto permite que "Linux-CLSD" responda verbalmente a los comandos del usuario.

En resumen, este script implementa un asistente de voz básico llamado "Linux-CLSD" que reconoce comandos de voz, realiza acciones específicas y proporciona respuestas auditivas al usuario. Puede ser ampliado y mejorado según las necesidades y requisitos específicos del proyecto.

### [Participa para desarrollar con nosotros el software ❤️](https://github.com/linux-clsd/linux-clsd/issues/2)

## Como usar L-CLSD ᵥ₋₁.₁
1. Instalar [Python](https://python.org)  
1.1 instalar ``` pip ``` (normalmente viene instalado con Python) ( ``` pip install pip ``` )  
1.2 Ejecuta ``` pip install SpeechRecognition && pip install pyttsx3 && pip install gTTS && pip install pygame ```
2. Instalar [Git](https://git-scm.com/)
3. Ejecuta ``` git clone https://github.com/linux-clsd/linux-clsd.git ```
4. Utiliza ``` chmod -R +w linux-clsd ``` para dar permisos de escritura en todo el directorio /linux-clsd 
5. Ahora ejecuta ``` cd linux-clsd ```
6. Para terminar usa ``` python3 ia.py ```

## Changelog
### v.1.1  
- Se han ajustado los parámetros ``` energy_threshold ``` y ``` dynamic_energy_adjustment_ratio ``` en el reconocedor de voz para mejorar la sensibilidad y adaptación al ruido ambiental.  

### v.1.0
- Hellow world

