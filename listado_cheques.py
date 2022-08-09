
from asyncio.windows_events import NULL
import csv
import time
from datetime import datetime

def obtenerDni():
  dni = NULL
  while not dni:
    dni = input("Ingrese el DNI del cliente (sin puntos): \n ".upper())
  return dni

def obtenerSalida():
  salida = ""
  while (salida != "PANTALLA" and salida != "CSV"):
    salida = str(input("Ingrese una salida: PANTALLA o CSV: \n")).upper()
  
  return salida

def obtenerTipo():
  tipo = NULL
  while (tipo != "EMITIDO" and tipo != "DEPOSITADO"):
    tipo = input("Ingrese el estado del cheque (EMITIDO o DEPOSITADO): \n".upper())  
  return tipo

def obtenerEstado():
  estado = input("Ingrese el estado del cheque: Aprobado, Rechazado o Pendiente (Opcional). \n".upper())
  return estado

def obtenerRangoFecha():
  fecha = input("Ingrese el rango de fecha del cheque en siguiente formato: xx-xx-xxxx:yy-yy-yyyy (Opcional) \n")
  return fecha

def procesarRango(fechaInput):
  if fechaInput:
    fechas = str(fechaInput).split(sep=':')
    fecha1 = datetime.strptime(fechas[0],"%d-%m-%Y")
    fecha2 = datetime.strptime(fechas[1],"%d-%m-%Y")
  
    return fecha1, fecha2
  else: return NULL, NULL
    
def timeStamp(fecha): 
  newFecha = datetime.strptime(fecha,"%d/%m/%Y")
  return newFecha
  
def procesarSalida(cheques, dni):
  salida = obtenerSalida()
  if salida == "PANTALLA":
    for i in range(len(cheques)):
      print(f''' ---------------------------------------------------------------------------------------
        Cheque N°{cheques[i]["NroCheque"]}
        
        Fecha de Emision: {cheques[i]["FechaOrigen"]}         Fecha de Pago: {cheques[i]["FechaPago"]}
        DNI: {cheques[i]["DNI"]}           Sucursal: {cheques[i]["CodigoSucursal"]}            Codigo: {cheques[i]["CodigoBanco"]}
        Cuenta de Origen: {cheques[i]["NumeroCuentaOrigen"]}               Cuenta de Destino: {cheques[i]["NumeroCuentaDestino"]}
        Tipo de Cheque: {cheques[i]["Tipo"]}         Estado del Cheque: {cheques[i]["Estado"]}
        Monto: {cheques[i]["Valor"]} $
      ---------------------------------------------------------------------------------''')

  if salida == "CSV":
    with open(f'cheques\{dni}_{datetime.now().strftime("%H-%M-%S")}.csv', "w") as archivo:    
      for cheque in cheques:
        archivo.writelines(f'Fecha de emision:{cheque["FechaOrigen"]}\n' f'Fecha de pago: {cheque["FechaPago"]}\n' f'Monto cheque: {cheque["Valor"]}\n' f'Cuenta de origen: {cheque["NumeroCuentaOrigen"]}\n')
      archivo.close()  
    

def procesarCheques():
  file=input('INGRESE EL NOMBRE (CON EL FORMATO) DEL ARCHIVO A PROCESAR (*Tengase en cuenta que el archivo deberá estar dentro de este):\n-->  '.upper())
  data= open(f'{file}','r') 
  csvReader=csv.DictReader(data) 
  
  dni = obtenerDni()
  tipo = obtenerTipo()
  estado = obtenerEstado()
  fecha = obtenerRangoFecha()

  fecha1, fecha2 = procesarRango(fecha)
  
  obj_cheque = {}
  cheques = list()
  for cheque in csvReader:
      fechaEmision = timeStamp(cheque["fechaEmision"])
      if cheque["Tipo"].upper() ==tipo.upper() and cheque['DNI'].replace(".", "").replace(".", "")==dni and (estado.upper() == cheque["Estado"].upper() or not estado) and ((not fecha1 and not fecha2) or (fechaEmision > fecha1 and fechaEmision <= fecha2)):
        obj_cheque["DNI"] = cheque["DNI"]
        obj_cheque["NroCheque"] = cheque["NroCheque"]
        obj_cheque["CodigoBanco"] = cheque["CodigoBanco"]
        obj_cheque["Tipo"] = cheque["Tipo"]
        obj_cheque["Estado"] = cheque["Estado"]
        obj_cheque["CodigoSucursal"] = cheque["CodigoSucursal"]
        obj_cheque["NumeroCuentaOrigen"] = cheque["NumeroCuentaOrigen"]
        obj_cheque["FechaOrigen"] = cheque["fechaEmision"]
        obj_cheque["Valor"] = cheque["Valor"] 
        obj_cheque["NumeroCuentaDestino"] = cheque["NumeroCuentaDestino"]
        obj_cheque["FechaPago"] = cheque["FechaPago"]
        
        cheques.append(obj_cheque.copy())        
  procesarSalida(cheques, dni)

procesarCheques()
