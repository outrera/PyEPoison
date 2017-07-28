import .ips
from py_gjapi import *

def get_exe():
	exe="Nombre de tu ejecutable sin el .exe"
	return exe
def file_to_var(file):
	File=open(str(file), "r")
	return File.readline()
	File.close()
def var_to_file(variable, filename):
	File=open(str(filename), "w")
	File.write(str(variable))
	File.close()
def usr_data():
	User = file_to_var("User.ini")
	Token = file_to_var("Token.ini")
	placeholder = GameJoltTrophy(User, Token, "Aqui va la id de tu juego", "aqui va la llave de tu juego")
	return placeholder
	#Establece la informacion del usuario
def Get_key():
	key = file_to_var("Key.ini")
	return key
	#Establece la key
#Inicia bloque de configuracion de murcielago/ Ignorar si no se usa murcielago
def IDU_MAIN():
	IDU="<aqui va la id de usuario que usa tu juego, usa 1 como valor de prueba>"
	return IDU
def Nombre_Juego():
	NJ = "<aqui va el nombre de tu juego>"
	return NJ
def Establecer_KY():
	KY = '<aqui va la key de tu juego, la encuentras al registrarte, usa 55c00763186270bc2f37037c666319cb para pruebas>'
	return KY
def Version_API():
	v = "1.1.1"
	return v
def Ver_Juego():
	v = "1.0"
	return v
#Termina bloque de configuracion de murcielago
def get_date_es():
	import datetime
	year=datetime.datetime.now()[0]
	month=datetime.datetime.now()[1]
	day=datetime.datetime.now()[2]
	hour=datetime.datetime.now()[3]
	minute=datetime.datetime.now()[4]
	second=datetime.datetime.now()[5]
	Message="El "+day+"/"+month+"/"+year+"/ a las "+hour+":"+minute+" con "+second+" segundos."
	return Message
def Send_to_debug(text):
	message=get_date_es()
	text="\n\n"+message+"\n"+text
	var_to_file(text, "debug.txt")
