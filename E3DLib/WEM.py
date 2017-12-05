# Windows executable management
import sys
import os
import psutil
import subprocess
import time
from E3DLib.gj_e3d_api import *
from E3DLib.archivo_de_configuracion import get_exe
from E3DLib.archivo_de_configuracion import usr_data
from E3DLib.archivo_de_configuracion import Send_to_debug
from subprocess import call as Run

def Create_game(level, var, args):
    major = sys.getwindowsversion().major
    minor = sys.getwindowsversion().minor
    executable = get_exe()
    if (major == 10) or (major == 6 and minor == 2):
        os.environ.update({"__COMPAT_LAYER": "WinXP"})
        # Si es win10 o win8 entra a modo compatibilidad
        if (major == 6 and minor == 2):
            # Si es win8 presenta este mensaje
            Send_to_debug("Tu sistema operatvio presenta fallas de compatibilidad,\n podrás ejecutar el juego pero el rendimiento no será el ideal.")

    if args == "Nada" or args == "nada" or args == "NADA":
        args = ("../"+executable+".exe -name Jugador -map "+level+" -variable Var1="+var+"-PrevMode")
    if args == "PickMode" or args == "pickmode" or args == "PICKMODE":
        args = ("../"+executable+".exe -name Jugador -map "+level+" -variable Var1="+var+"-PickMode")
    proc = Run(args, shell=False, env=os.environ)
    start_game()
    PID = proc.pid
    try:
        # Intenta obtener el estado del proceso.
        State = psutil.Process(PID)
    except:
        # Mensaje si no lo ha encontrado :c
        Send_to_debug("No se encontró el proceso")

    while psutil.pid_exists(PID):
        # Si el proceso existe
        if State.status:
            keep_active()
            print(State.status)
            print(PID)
            time.sleep(3)
