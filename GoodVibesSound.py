import time
import psutil
import pygame
import os
import random


processes = ['cursor.exe','idea64.exe', 'clion64.exe','Code.exe', 'geany.exe','netbeans.exe','devcpp.exe','pycharm64.exe']
pygame.mixer.init()
path = r"C:\Users\Doia\Documents\musica"

# Buscamos el proceso en cuestion
def find_processes():
    #Usamos una bandera, ya que no haremos nada distinto dependiendo del programa
    try:
        for p in psutil.process_iter(attrs=['name']):
            if p.info['name'] in processes:
                return True
            #Optimizamos la busqueda
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
        return False


def load_music (path):
    #arroja un arreglo
    choice= random.choice(os.listdir(path))
    print(choice)
#Escogemos una canción al azar
    pygame.mixer.music.load(path+"\\"+choice)
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     time.sleep(1)


def main():
    count = 0
    while True:
        ide_abierto = find_processes()
        #Mientras haya encontrado un process
        if ide_abierto and not pygame.mixer.music.get_busy():
            if count < 2:
                load_music(path)
                count += 1
            else:
                pygame.mixer.music.stop()
                break

        elif not ide_abierto:
              if pygame.mixer.music.get_busy():
                 pygame.mixer.music.stop()
                #Busca el proceso, en teoria no debe de haber nada hasta este punto
        time.sleep(5)



if __name__ == '__main__':
    main()









