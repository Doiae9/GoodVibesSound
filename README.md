# GoodVibesSound: El Gancho Musical para Programar
> Un script ligero de Python diseñado para actuar como un "gancho" (cue) para iniciar hábitos de programación, inspirado en el libro "Hábitos Atómicos".

- El objetivo es simple: al abrir un IDE de programación, el script detecta la acción y reproduce automáticamente un breve playlist (2 canciones) para preparar la sesión de trabajo.

## 🎯 ¿Por qué este proyecto?
> Este script resuelve dos problemas:

- Fricción al Empezar: Ayuda a crear una señal clara para el cerebro de que es "hora de programar", haciendo más fácil entrar en estado de flow.
- Evitar la Fatiga Auditiva: A diferencia de un reproductor infinito, este script es intencionalmente limitado. Toca dos canciones y luego se detiene automáticamente, ya que el propósito no es que sea un reproductor, esto esta diseñado para que al momento de abrir un IDE lo primero que se escuche sea música. 
- Esto se trata de poder reproducir música antes que nada, antes de que se pueda abrir el navegador o spotify para esuchar música.

## ✨ Características (MVP)
- Detección de IDEs: Monitorea los procesos del sistema en busca de IDEs populares (VS Code, IntelliJ, PyCharm, etc.).
- Playlist de "Arranque": Al detectar un IDE, reproduce 2 canciones aleatorias desde una carpeta local.
- Auto-detención: Después de que la segunda canción termina (o empieza, según la lógica), el script termina su ejecución (break) para liberar el 100% de los recursos del sistema.
- Ligero: Corre como un script de fondo sin consola visible (compilado con PyInstaller).

## ⚙️ Cómo Funciona
El script utiliza un bucle principal que se ejecuta cada pocos segundos:
- Detección (Eficiente): Usa psutil con attrs=['name'] y manejo de excepciones (try...except) para escanear eficientemente los procesos en ejecución sin consumir alto CPU.
- Lógica de Estado: Utiliza el estado de pygame.mixer.music.get_busy() como una "bandera" para saber si debe o no reproducir música.
- Contador de Playlist: Un contador interno (count) lleva la cuenta de cuántas canciones se han reproducido.
- Salida Limpia: Una vez que count llega a 2, el script ejecuta un break para salir del while True, finalizando el proceso y liberando la memoria.

### 🛠️ Tecnologías Utilizadas
- Python 3.13
- psutil: Para la detección de procesos del sistema operativo.
- pygame (mixer): Para la reproducción de audio.
- PyInstaller: Para compilar el script en un archivo .exe ejecutable e independiente.

### 📦 Instalación (Como servicio de inicio)
- La forma más sencilla de usarlo es ejecutar el .exe compilado al iniciar Windows:
- Compilar el proyecto usando PyInstaller (asegúrate de incluir los hooks para pygame y psutil):

```bash
pyinstaller --onefile --noconsole --hidden-import=pygame --paths="C:\ruta\a\tu\site-packages" GoodVibesSound.py
```
- Presionar Win + R y escribir shell:startup.
- Pegar un acceso directo al .exe (generado en la carpeta dist) dentro de esta carpeta de "Inicio".
- Reiniciar el equipo. El script se ejecutará una vez, esperará a que abras un IDE, tocará sus dos canciones y se cerrará.
