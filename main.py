import psutil
import playsound

processes = ['pycharm64.exe','cursor.exe','idea.exe', 'Clion.exe']

# Buscamos el proceso en cuestion
def find_processes():
    for p in psutil.process_iter(['name', 'status']):
        if p.info['status'] == psutil.STATUS_RUNNING and p.info['name'] in processes:
            return p
    return None



#find_processes()
# for process in processes:
    #    if psutil.pid_exists(process):
    #for p in psutil.process_iter(['name', 'status']):
     #   if p.info['status'] == psutil.STATUS_RUNNING:
      #  if p.info['name'] == 'pycharm64.exe':
       #     print(p.info['name'])