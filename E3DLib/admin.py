import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def runAsAdmin(args):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, args, None, 1)


def setup_ports():
    import os
    Run('dism /Online /enable-feature /FeatureName:"LegacyComponents" /NoRestart')
    # Activa los componentes heredados
    Run('dism /Online /enable-feature /FeatureName:"DirectPlay" /NoRestart')
    # Activa DirectPlay
    locate = os.path.dirname(os.path.abspath('../python/'))
    handle = open(locate + "\FRST.txt", "r+", encoding="utf8")
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
