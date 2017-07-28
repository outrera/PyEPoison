from E3dLib.Mur import Exportar_datos_partida
from E3dLib.archivo_de_configuracion import file_to_var, var_to_file

index = file_to_var("Solicitud.ini")
try:
    Exportar_datos_partida(index)
except:
    var_to_file("False", "Indice.ini")
