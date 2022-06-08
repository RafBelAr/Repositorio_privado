#!/usr/bin/python3

import os
import sys
import time
import signal
import openpyxl
import datetime

strdate = "12/31/22"
fecha = datetime.datetime.strptime(strdate, "%m/%d/%y")

def def_handler(sig, frame):
    print("[!]Saliendo...\n\n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def comprobacion_archivos():
    if (len(sys.argv) < 2):
        print("[!] Error, pasa los argumentos necesarios. \n 'python3 parser.py <archivo>'\n\n")
        sys.exit(1)

    string = sys.argv[1]

    if (string[-4:] != "xlsx"):
        print("[!] Error en el tipo! Tiene que ser xlsx\n[!] Saliedo...\n\n\n")
        sys.exit(1)


def exit(i):
    sys.exit(i)

def comprobacion_celdas(fila):
    #En un principio type(celda) = datetime
    celda = fila[0].value
    #En caso de ser 2018 o menor y tener el otro en null
    if celda.date().year < (datetime.datetime.now().date().year - 3):
        if fila[3].value == "AÑO PRORROGA (FINALIZA 31/12/2022)":
            print(f'Cambiando {fila[2].value} por {fecha}')
            fila[1].value = fecha.date()

    if celda.date().year > (datetime.datetime.now().date().year - 4):
        suma = str(fila[0].value.date().year + 3)
        print (suma)
        print(type(suma))
        new_date = f"31/12/{suma[-2:]}"
        print(type(new_date))

        print("traza\n\n\n")
        fecha_cambiada = datetime.datetime.strptime(new_date,"%d/%m/%y")
        fila[1].value = fecha_cambiada.date()

        #fila[1].value =  


def parser():
    excel_document = openpyxl.load_workbook(sys.argv[1])

    sheet = excel_document['Hoja1']

    fecha_inicio = sheet['E2':'H1031']
    fecha_fin = sheet['F2':'F1031']

    fechas = sheet['E2':'H1031']


    # 0 Fecha inicio // 1 Fecha fin // 2 Comentarios1 // 3 Comentarios2


    for row in fechas:
        if row[1].value == None:
            #La celda es null
            comprobacion_celdas(row)

    excel_document.save("generado.xlsx")







if __name__ == "__main__":
    print("[+] Iniciando script...\n")

    comprobacion_archivos()

    parser()

    exit(0)
