"""Simulación de Logs Generados por un Servicio: Crea un script que genere logs simulados en formato JSON, incluyendo la fecha, nombre del servicio,
nivel de severidad y un mensaje descriptivo. Haz que los logs se impriman en la terminal cada 5 segundos."""

import json #para el formato
import time #para esperas
from datetime import datetime  #para fecha y hora
import random #para los niveles de severidad


def generar_log():
    
    #obtenemos fecha y hora 
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #definimos los niveles de severidad
    
    niveles_sev = ['INFO', 'ADVERTENCIA', 'ERROR', 'CRITICO', 'AUSILIO POLISIA']
    
    #creamos un diccionario con los datos del log
    
    formato_log ={
        
        'fecha': fecha_hora,
        'service': "LuceroService",
        'nivel_severidad': random.choice(niveles_sev),
        'mensaje': "Este es un simulador de log"
        
    }
    
    
    #convertimos el diccionario en una cadena JSON 
    
    return json.dumps(formato_log, ensure_ascii=False)


def imprimir_logs():
    while True:
        
        #Generar un log
        log = generar_log()
        
        
        #imprimimos en la terminar
        print(log)
        
        #Esperar 5 segundos antes del siguiente log
        time.sleep(5)
        
        
if __name__ == '__main__':
    imprimir_logs()
