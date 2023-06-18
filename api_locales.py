import requests
import json

url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'


def mostrar():
    peticion = requests.get(url)
    locales = json.loads(peticion.content)
    print("{:<15} {:<10} {:<10} {:<10} {:<15} {:<30} {:<20} {:<100} {:<15} {:<15} {:<15} {:<50} {:<50} {:<20} "
        .format('Fecha','id_loc','Fk_region','Fk_comuna','Fk_localidad','Local_nombre','Comuna_nombre',
        'local direccion','Hora_apertura','Hora_cierre','Telefono','Latitud','longitud','dia_func'))
    #num= 0
    for local in locales:
        #num = num+1
        print("{:<15} {:<10} {:<10} {:<10} {:<15} {:<30} {:<20} {:<100} {:<15} {:<15} {:<15} {:<50} {:<50} {:<20}".format(local['fecha'],local['local_id'],
        local['fk_region'],local['fk_comuna'],local['fk_localidad'],local['local_nombre'],local['comuna_nombre'],
        local['local_direccion'],local['funcionamiento_hora_apertura'],local['funcionamiento_hora_cierre'],
        local['local_telefono'],local['local_lat'],local['local_lng'],local['funcionamiento_dia']))
        
        
mostrar()
    
    
    