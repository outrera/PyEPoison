import urllib.request
from E3DLib.ips import *
from xml.etree import ElementTree
from xml.dom.minidom import parseString
import E3DLib.archivo_de_configuracion
import E3DLib.WEM

# inicia bloque de funciones de "sistema"
# (No están hechas para ser utilizadas por los usuarios, aunque se pueden utilizar para crear otro código


def Ob_Mapa():
    Mapa = file_to_var("Mapa.ini")
    return Mapa


def Leer_salida(xml): # Lee la entrada en formato XML
    dom = parseString(xml) # Lee el archivo XML
    data = dom.getElementsByTagName('numero')[0].childNodes[0].data #Busca en el arhcivo XML los elementos de la etiqueta "numero"
    return data


def Ob_MJ():
    Modo = file_to_var("Modo.ini")
    return Modo


def Mensajes_salida(input):
    numero = input
    if numero == 0:
        return "Partida creada"
    if numero == 1:
        return "La información del servidor no coincide con la del cliente"
    if numero == 2:
        return "Partida no creada"
    if numero == 3:
        return "No se encontraron partidas"
    if numero == 4:
        return "La operación no existe, verificar configuración"
    if numero == 5:
        return "Formato solicitado no existente"    # Error para desarrolladores
    if numero == 6:
        return "Modo de juego no válido"
    if numero == 7:
        return "La caducidad debe ser un valor mayor a cero" # Error para desarrolladores
    if numero == 8:
        return "La IP no puede estar vacía" # Error para desarrolladores, asegurate de estar usando el módulo de ips correcto junto con murcielago
    if numero == 9:
        return "El nombre del mapa no puede estar vacío"
    if numero == 10:
        return "El nombre del juego no puede estar vacío"
    if numero == 11:
        return "La versión del juego no puede estar vacía" # Error para desarrolladores
    if numero == 12:
        return "No hay conexión con la base de datos"
    if numero == 13:
        return "No hay actualizaciones disponibles"

# Termina bloque de funciones de "sistema"


# Incia el bloque de funciones para usuarios.

def Iniciar_servidor(Var): # 1 es para partida pública, 2 es para partida en lan
    if Var == 1:
        ip = get_ext_ip() # Es una función, no se modifica
    if Var == 2:
        ip = get_lan_ip()
    VERSION_API = Version_API()
    IDU = IDU_MAIN() # No se modifica
    KY = Establecer_KY()
    NJ = Nombre_Juego()
    Map = Ob_Mapa()
    M_Juego = Ob_MJ()
    N_Partida = file_to_var("NombrePartida.ini")
    with urllib.request.urlopen("http://www.comunidad-e3d.com/api/murcielago/"+VERSION_API+".php?op=cre&idu="+IDU+"&ft=0&ky="+KY+"&nj="+NJ+"&ip="+ip+"&mj="+M_Juego+"&m="+Map+"&vj=1.3&np="+N_Partida) as response:
        html = response.read()
    numero = Leer_salida(html)
    salida = Mensajes_salida(numero)
    Send_to_debug(salida)


def Exportar_datos_partida(indice):
    KY = Establecer_KY()
    IDU = '1'
    NJ = Nombre_Juego()
    VERSION_API = Version_API()
    with urllib.request.urlopen("http://www.comunidad-e3d.com/api/murcielago/"+VERSION_API+".php?op=lis&idu="+IDU+"&ft=2&ky="+KY+"&nj="+NJ+"&ip="+ip+"&mj="+M_Juego+"&m="+Map+"&vj=1.3&ca=60&") as consult:
        string = json.loads(consult.read())
    NPartida = string[indice]['nombrePartida']
    P_ip = string[indice]['ip']
    M_Juego = string[indice]['modoJuego']
    Mapa = string[indice]['mapa']
    VJuego = string[indice]['versionJuego']

    var_to_file(NPartida, "Nombre.temp")
    var_to_file(M_Juego, "Modo.temp")
    var_to_file(Mapa, "Mapa.temp")
    var_to_file(VJuego, "Version.temp")
    try:
        with open("/bmp/HUD/overlays/" + Mapa + "_overlay.jpg", "r") as MP:
            var_to_file(MP, "/bmp/HUD/overlays/menu_overlay_30.jpg")
        MP.close()
    except IOError:
        MP = open("/bmp/HUD/overlays/overlay_base.bmp", "r")
        var_to_file(MP, "/bmp/HUD/overlays/menu_overlay_30.bmp")
        Send_to_debug("Imagen no encontrada, puede que no tengas el mapa o que no se haya proveido una preview del mismo")
    return P_ip


def Unirse_servidor():
    User = file_to_var("User.ini")
    PERS = file_to_var("Pers.ini")
    Map = file_to_var("Map.ini")
    EQUIPO = file_to_var("Team.ini")
    Mod = file_to_var("Mod.ini")
    exe = get_exe()
    args = exe + ".exe -name " + User + " -map " + Map + " -server -personaje " + PERS+ " -equipo "+EQUIPO+" -modojuego "+Mod+" -PrevMode"
    Create_game("nada", "nada", args)


def Unirse_cliente(ip):
    User = file_to_var("User.ini")
    PERS = file_to_var("Pers.ini")
    Map = file_to_var("Mapa.temp")
    EQUIPO = file_to_var("Team.ini")
    Mod = file_to_var("Modo.temp")
    args = exe+".exe -name "+User+" -map "+Map+" -client "+ip+"-personaje "+PERS+" -equipo "+EQUIPO+" -modojuego "+Mod+" -PrevMode"
    Create_game("nada", "nada", args)


# Termina el bloque de funciones para usuarios.
