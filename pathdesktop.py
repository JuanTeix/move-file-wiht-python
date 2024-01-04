import os

def obtener_ruta_escritorio():
    sistema_operativo = os.name  # Obtener el nombre del sistema operativo
    
    if sistema_operativo == 'posix':  # Sistema operativo tipo Unix (Linux, macOS)
        ruta_escritorio = os.path.expanduser("~/Desktop")
    elif sistema_operativo == 'nt':  # Windows
        ruta_escritorio = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        ruta_escritorio = None
    
    return ruta_escritorio

ruta = obtener_ruta_escritorio()
