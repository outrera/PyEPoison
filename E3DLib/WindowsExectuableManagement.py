import sys
import os
import psutil
import subprocess
import time
import .gj_e3d_api
import .archivo_de_configuracion
from py_gjapi import closeSession

def Create_game(level,var,args):
    major=sys.getwindowsversion().major
    minor=sys.getwindowsversion().minor
    if (major == 10) or (major == 6 and minor == 2):
        os.environ.update({"__COMPAT_LAYER": "WinXP"})  # Si es win10 o win8 entra a modo compatibilidad
        if (major == 6 and minor == 2): #Si es win8 presenta este mensaje
            Send_to_debug("Tu sistema operatvio presenta fallas de compatibilidad,\n podrás ejecutar el juego pero el rendimiento no será el ideal.")

    executable=get_exe()
    if args == "Nada" or args == "nada" or args == "NADA":
        args=(executable+".exe -name Jugador -map "+level+" -variable Var1="+var+"-PrevMode")
    proc=subprocess.Popen(args, shell=True, env=os.environ)
    start_game()
    PID= proc.pid
    try: #Intenta obtener el estado del proceso.
	   State = psutil.Process(PID)
    except: #Mensaje si no lo ha encontrado :c
	   Send_to_debug("No se encontró el proceso")

   while psutil.pid_exists(PID): #Si el proceso existe
    if State.status:
        keep_active()
		print(State.status)
		print(PID)
		time.sleep(3)
   usr_data().closeSession()
