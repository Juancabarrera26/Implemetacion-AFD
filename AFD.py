import sys
import os

def procesar_cadena(linea_archivo):
    cadena = linea_archivo.strip()

    if not cadena:
        return False

    estado = 'q1'
    
    for char in cadena:
        if estado == 'q1':
            if char == '0':
                estado = 'q2'
            elif char == '1':
                estado = 'q3'
            else:
                return False
                
        elif estado == 'q2':
            if char == '0' or char == '1':
                estado = 'q2'
                
        elif estado == 'q3':
            if char == '0' or char == '1':
                estado = 'q3'

    return estado == 'q2'

if len(sys.argv) < 2:
    print("Falta el archivo")
else:
    nombre = sys.argv[1]
    
    if os.path.exists(nombre):
        archivo = open(nombre, 'r')
        for linea in archivo:
            if procesar_cadena(linea):
                print("ACEPTA")
            else:
                print("NO ACEPTA")
        archivo.close()
    else:
        print("Archivo no encontrado")
