import psutil
import subprocess
import time
from pathlib import Path
#import gj_e3d_api
args="tpack.exe"
proc=subprocess.Popen(args)
PID= proc.pid
#my_file = Path("Closed.txt")
try: #Intenta obtener el estado del proceso.
	State = psutil.Process(PID)
except: #Mensaje si no lo ha encontrado :c
	print("Process couldn't be found")
while psutil.pid_exists(PID): #Si el proceso es un zombie
	if State.status: 
			#keep_active()
		
		print(State.status)
		print(PID)
		time.sleep(3)
	#if not State.status:
	#	break


#my_file = Path("Closed.txt")
#if my_file.is_file():
#if my_file.is_file():