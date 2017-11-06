"""
Este archivo contiene nombres legibles en español,
para su uso por usuarios de Entidad3D
también incluye funciones predefinidas
que pueden ser utiles para manejar por comandos algunos
eventos del juego, como son el inicio de una partida o unirse a un servidor
"""
import E3DLib.ips
from E3DLib.archivo_de_configuracion import file_to_var as ARCH_A_VAR
from E3DLib.archivo_de_configuracion import var_to_file as VAR_A_ARCH
from E3DLib.gj_e3d_api import login as LOGIN
from E3DLib.gj_e3d_api import give_trophy as DAR_TROFEO
from E3DLib.gj_e3d_api import start_game as INICIAR_SESION
from E3DLib.gj_e3d_api import keep_active as MANTENER_ACTIVO
from E3DLib.gj_e3d_api import keep_logged as MANTENER_SESION
from E3DLib.gj_e3d_api import save_server_score as GUARDAR_PUNT_SERV
from E3DLib.gj_e3d_api import save_clients_score as GUARDAR_PUNT_CL
from E3DLib.gj_e3d_api import get_max_scores as CONS_PUNT_MAX
from E3DLib.gj_e3d_api import get_data as CONS_DATA
from E3DLib.gj_e3d_api import store_Data as GUARDAR_PARTIDA
from E3DLib.gj_e3d_api import get_scores as CONS_PUNT
from E3DLib.gj_e3d_api import get_tables as CONS_TABLAS
import E3DLib.Mur
from E3DLib.FlagSoundLib import flag_sound as SOND_FLAG
from E3DLib.WEM import Create_game as CREAR_JUEGO
