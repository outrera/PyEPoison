import psutil
import subprocess
import time
import gj_e3d_api
import archivo_de_configuracion
def Create_game_online(executable,
def Create_game_offline(executable,level,var,bruh)
	args=(executable+".exe -name Jugador -map "+level+" -variable Var1="+var+"-PrevMode")
	proc=subprocess.Popen(args)
	PID= proc.pid
	try: #Intenta obtener el estado del proceso.
		State = psutil.Process(PID)
	except: #Mensaje si no lo ha encontrado :c
		print("Process couldn't be found")
	while psutil.pid_exists(PID): #Si el proceso es un zombie
		if State.status: 
			keep_active()
			print(State.status)
			print(PID)
			time.sleep(3)
