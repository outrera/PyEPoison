"""
Este archivo contiene nombres legibles en español, para su uso por usuarios de Entidad3D
también incluye funciones predefinidas que pueden ser utiles para manejar por comandos algunos
eventos del juego, como son el inicio de una partida o unirse a un servidor
"""
import ips
from archivo_de_configuracion import file_to_var as ARCH_A_VAR
from archivo_de_configuracion import var_to_file as VAR_A_ARCH
from gj_e3d_api import login as LOGIN
from gj_e3d_api import give_trophy as DAR_TROFEO
from gj_e3d_api import start_game as INICIAR_SESION
from gj_e3d_api import keep_active as MANTENER_ACTIVO
from gj_e3d_api import keep_logged as MANTENER_SESION
from gj_e3d_api import save_server_score as GUARDAR_PUNT_SERV
from gj_e3d_api import save_clients_score as GUARDAR_PUNT_CL
from gj_e3d_api import get_max_scores as CONS_PUNT_MAX
from gj_e3d_api import get_data as CONS_DATA
from gj_e3d_api import store_Data as GUARDAR_DATA
from gj_e3d_api import get_scores as CONS_PUNT
from gj_e3d_api import get_tables as CONS_TABLAS
import Mur
from FlagSoundLib import flag_sound as SOND_FLAG
from WindowsExecutableManagement import Create_game as CREAR_JUEGO
def INICIAR_PARTIDA(nivel,variable):
    INICIAR_SESION()
    CREAR_JUEGO(nivel,variable)
def CAMBIAR_NIVEL(nivel,variable):
    CREAR_JUEGO(nivel,variable)
