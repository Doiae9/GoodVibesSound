import time
import psutil
import pygame
import os
import random


processes = ['pycharm64.exe','cursor.exe','idea.exe', 'Clion.exe']

# Buscamos el proceso en cuestion
#
def find_processes():
    for p in psutil.process_iter(['name', 'status']):
        if p.info['status'] == psutil.STATUS_RUNNING and p.info['name'] in processes:
            return p
    return None


path = r"C:\Users\Doia\Documents\musica"

def load_music (path):
    #arroja un arreglo
    choice= random.choice(os.listdir(path))
    print(choice)
    pygame.mixer.init()
#Escogemos una canción al azar
    pygame.mixer.music.load(path+"\\"+choice)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

load_music(path)
#todo juntar condicionales

#todo ejecutar en segundo plano

#todo ejecutar al encender la computadora

#todo ejecutar solo una vez?


