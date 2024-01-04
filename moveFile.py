import os
import shutil
from pathdesktop import obtener_ruta_escritorio



def moveFile():
    path_desktop = obtener_ruta_escritorio()
    path_in = os.path.join( path_desktop+"/File_IN")
    path_out = os.path.join( path_desktop+"/File_OUT")


    if not os.path.isdir(path_in):
        message = 'La Carpeta IN no existe'
        print(message)
        return message
    elif not os.path.isdir(path_out):
        message = 'La Carpeta OUT no existe'
        print(message)
        return message
    else:
        contenidos= os.listdir(path_in)
        for elemento in contenidos:
            shutil.move(path_in+"/"+elemento, path_out)
            message = 'Los Archivos se han pasado a la carpeta destino'
            print(message)
            return message


