# Windows executable management
import sys
import os
import psutil
import subprocess
import time
from E3DLib.gj_e3d_api import *
from E3DLib.archivo_de_configuracion import get_exe
from E3DLib.admin import is_admin
from E3DLib.admin import runAsAdmin
from subprocess import call as Run

def Create_game(level, var, args):
    if not is_admin():
            runAsAdmin()
    major = sys.getwindowsversion().major
    minor = sys.getwindowsversion().minor
    executable = get_exe()
    if (major == 10) or (major == 6 and minor == 2):
        locate = os.path.dirname(os.path.abspath('../python/'))
        handle = open(locate + "\FRST.txt", "r+", encoding="utf8")
        firsttime = int(handle.readline())
        if firsttime is 1:
            Run('dism /Online /enable-feature /FeatureName:"LegacyComponents" /NoRestart')
            # Activa los componentes heredados
            Run('dism /Online /enable-feature /FeatureName:"DirectPlay" /NoRestart')
            # Activa DirectPlay
            locate = os.path.dirname(os.path.abspath('../python/'))
            # Localiza el directorio en el que está instalado el juego
            Run('netsh advfirewall firewall add name=\"' + executable + '\" dir=in action=allow program=\"'+ locate + executable +'.exe\" enable=yes')
            # Añade una regla para el fitewall de windows
            Run('netsh advfirewall firewall add rule name=\"E3D TCP Port 47624\" dir=in action=allow protocol=TCP localport=47624')
            Run('netsh advfirewall firewall add rule name=\"E3D TCP Port 47624\" dir=out action=allow protocol=TCP localport=47624')
            Run('netsh advfirewall firewall add rule name=\"E3D UDP Port 47624\" dir=in action=allow protocol=UDP localport=47624')
            Run('netsh advfirewall firewall add rule name=\"E3D UDP Port 47624\" dir=out action=allow protocol=UDP localport=47624')
            for ports in range(2300, 2401):
                Run('netsh advfirewall firewall add rule name=\"E3D TCP Port ' + str(ports) + '\" dir=in action=allow protocol=UDP localport='+str(ports))
                Run('netsh advfirewall firewall add rule name=\"E3D UDP Port ' + str(ports) + '\" dir=out action=allow protocol=UDP localport='+str(ports))
            # Añade las reglas de puertos UDP y TCP de entrada y salida.
            handle.write("0")
        handle.close()
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
    PID= proc.pid
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
