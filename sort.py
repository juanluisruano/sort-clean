# -*- coding: utf-8 -*-
"""
BOT_ONE chatbot


@author: Juan l Ruano


# IMPORTACION DE LIBRERIAS NECESARIAS

import numpy as np
import tensorflow as tf
import re 
import time 

#
lines = open (r'C:\Users\juan\movie_lines.txt', encoding ='utf-8', errors = 'ignore').read().split('\n')
conversations = open (r'C:\Users\juan\movie_conversations.txt', encoding ='utf-8', errors = 'ignore').read().split('\n')



linea_id =  {}  # AQUI CREO E iNICIALIZO el DICCIONARIO necesario para la IA

for line in lines: 
    
    _line = line.split(' +++$+++ ')

    if len(_line) == 5:
        """ obtenemos los valores de las columnas 0(1)id y 4(5)conversaciones"""
        linea_id[_line[0]] = _line[4]


conversations_ids = [] 
for conversation in conversations[:-1]:    # se coje todo el conjunto de conversaciones, menos uno, ponemos -1 significa la ultima fila de conversaciones [].
        _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")       # se crea variable local temporal ,limpia solo para tener la última parte ,dividimos y obtenemos último elemento de la division
         #con [1:-1] eliminamos los corchetes , .replace ("'","") cambia las comillas.
        #.replace(" ","") cambia espacios 
        """ Con append , añadimos a toda la lista (conversations_ids) la variable que ha limpiado y sustituido caracteres (_conversation)"""
        conversations_ids.append(_conversation.split(','))
        
preguntas = [ ] #creamos e inicializamos las 2 variables
respuestas = [ ]

for conversation in conversations_ids:
        for i in range(len(conversation)-1):
            #añadimos las preguntas. se usa el diccionario linea_id. mapea por indice
            preguntas.append(linea_id[conversation[i]])
            #añadimos las respuestas. se usa el diccionario linea_id. mapea por indice
            respuestas.append(linea_id[conversation[i+1]]) 
            
            
