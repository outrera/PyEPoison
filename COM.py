from xml.etree import ElementTree as ET
from xml.dom.minidom import parseString
import xml.etree.ElementTree
with open("Test.xml") as lista:
    ress = lista.read()

print(ress)
Alfa = parseString(ress)
root = Alfa.getroot()
for Partida in root.iter('Partida'):
	print(Partida.attrib)
