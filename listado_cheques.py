
import csv
import time
import datetime

def procesarCheques():
  file=input('INGRESE EL NOMBRE DEL ARCHIVO .CSV A PROCESAR (*Tengase en cuenta que el csv deberá estar dentro de este):\n-->  '.upper())
  data= open(f'{file}.csv','r') 
  csvReader=csv.DictReader(data) 
  
  operaciones=input('INGRESE LA OPERACION A REALIZAR:\n 1) --Ver Cheques Aprobados\n 2) ---Ver cheques rechazados\n 3) ---Ver todos los cheques\n 4) ---Exportar todos mis depositos\n 5) ---Salir\n--> '.upper())
  def timeStamp(fecha): 
    newFecha= time.mktime(datetime.datetime.strptime(fecha,"%d/%m/%Y").timetuple())
    return newFecha
  def switcher(opcion):
    
    def opcion1():
     datoPorConsola=input('Ingrese su dni \n--- '.upper())
     print('Sus cheques Aprobados son:')
     for cheque in csvReader:
        if cheque['DNI']==datoPorConsola and cheque['Estado']=='Aprobado':
          print(f'''-------------------------------------------------------------------------------------------------
            Cheque N°: {cheque["NroCheque"]}                          EMISOR: {cheque['Nombre']} {cheque['Apellido']} 

            Fecha de Emision: {timeStamp(cheque["fechaEmision"])}         Fecha de Pago: {timeStamp(cheque["FechaPago"])} 

            DNI: {cheque["DNI"]}     BANCO: {cheque['Banco']}       Sucursal: {cheque["CodigoSucursal"]}            Codigo: {cheque["CodigoBanco"]}

            Cuenta de Origen: {cheque["NumeroCuentaOrigen"]}               Cuenta de Destino: {cheque["NumeroCuentaDestino"]}

            Tipo de Cheque: {cheque["Tipo"]}         Estado del Cheque: {cheque["Estado"]}

            Monto: ${cheque["Valor"]} 
            --------------------------------------------------------------------------------------------------''')         
          operacion=input('\nINGRESE LA OPERACION A REALIZAR:\n1)--- Exportar \n2)--- Salir\n--> '.upper())
          if operacion=='1' or operacion=='EXPORTAR':
           nombreArchivo=input('Ingrese el nombre de su archivo CSV\n'.upper())
           fieldnames = ['Nombre','Apellido','Cheque N°', 'EMISOR','FECHA EMISION','FECHA PAGO','DNI','BANCO','Sucursal','Codigo','Cuenta Origen','Cuenta destino','Tipo cheque','Estado','Valor']

           with open(f'{nombreArchivo}.csv', 'w',) as csvfile:
             writer=csv.writer(csvfile)
             writer.writerow(fieldnames)
             for cheque in csvReader:

                if cheque['DNI']==datoPorConsola :
                 try:
                
                  data=[cheque['Nombre'],cheque['Apellido'],cheque['NroCheque'],cheque['Banco'],cheque['NumeroCuentaDestino'],cheque['NumeroCuentaOrigen'],cheque['Valor'],cheque['fechaEmision'],cheque['FechaPago'],cheque['Fondos'],cheque['Estado'],cheque['Tipo']]
                  writer.writerow(data)
                  print('Archivo creado exitosamente')

                 except:
                  print('Lo sentimos ha habido un problema')
          elif operacion=='2' or operacion=='SALIR':
            break
    def opcion2():
      datoPorConsola=input('Ingrese su dni \n--- '.upper())
      print('Estos son sus cheques Rechazados:')
      for cheque in csvReader:
           if cheque['DNI']==datoPorConsola and cheque['Estado']=='Rechazado':
            print(f'''-------------------------------------------------------------------------------------------------
            Cheque N°: {cheque["NroCheque"]}                          EMISOR: {cheque['Nombre']} {cheque['Apellido']} 

            Fecha de Emision: {timeStamp["fechaEmision"]}         Fecha de Pago: {timeStamp(cheque["FechaPago"])} 

            DNI: {cheque["DNI"]}     BANCO: {cheque['Banco']}       Sucursal: {cheque["CodigoSucursal"]}            Codigo: {cheque["CodigoBanco"]}

            Cuenta de Origen: {cheque["NumeroCuentaOrigen"]}               Cuenta de Destino: {cheque["NumeroCuentaDestino"]}

            Tipo de Cheque: {cheque["Tipo"]}         Estado del Cheque: {cheque["Estado"]}

            Monto: ${cheque["Valor"]} 
            --------------------------------------------------------------------------------------------------''')    
    def opcion3 ():
      datoPorConsola=input('Ingrese su dni \n--- '.upper())
      print('Estos son todos sus cheques:')
      for cheque in csvReader:
           if cheque['DNI']==datoPorConsola and cheque['Estado']:
            print(f'''-------------------------------------------------------------------------------------------------
 Cheque N°: {cheque["NroCheque"]}                          EMISOR: {cheque['Nombre']} {cheque['Apellido']} 
 
 Fecha de Emision: {timeStamp(cheque["fechaEmision"])}         Fecha de Pago: {timeStamp(cheque["FechaPago"])} 

 DNI: {cheque["DNI"]}     BANCO: {cheque['Banco']}       Sucursal: {cheque["CodigoSucursal"]}            Codigo: {cheque["CodigoBanco"]}

 Cuenta de Origen: {cheque["NumeroCuentaOrigen"]}               Cuenta de Destino: {cheque["NumeroCuentaDestino"]}

 Tipo de Cheque: {cheque["Tipo"]}         Estado del Cheque: {cheque["Estado"]}

 Monto: ${cheque["Valor"]} 
 --------------------------------------------------------------------------------------------------''')
    def opcion4():
        datoPorConsola=input('Ingrese su dni \n--- '.upper())
        nombreArchivo=input('Ingrese el nombre de su archivo CSV\n'.upper())
        fieldnames = ['Nombre','Apellido','Cheque N°', 'EMISOR','FECHA EMISION','FECHA PAGO','DNI','BANCO','Sucursal','Codigo','Cuenta Origen','Cuenta destino','Tipo cheque','Estado','Valor']
        with open(f'{nombreArchivo}.csv', 'w',) as csvfile:
         writer=csv.writer(csvfile)
         writer.writerow(fieldnames)
         for cheque in csvReader:
           
            if cheque['DNI']==datoPorConsola :
             try:
           
              data=[cheque['Nombre'],cheque['Apellido'],cheque['NroCheque'],cheque['Banco'],cheque['NumeroCuentaDestino'],cheque['NumeroCuentaOrigen'],cheque['Valor'],cheque['fechaEmision'],cheque['FechaPago'],cheque['Fondos'],cheque['Estado'],cheque['Tipo']]
              writer.writerow(data)
              print('Archivo creado exitosamente')
              
             except:
              print('Lo sentimos ha habido un problema')
      


              
              
              
    def opcion5():
      print('Gracias por elegirnos!')
      exit()

    switcher = {
        '1': opcion1,
        '2': opcion2,
        '3': opcion3,
        '4': opcion4,
        '5': opcion5
    }
  
    func= switcher.get(opcion,lambda: "Lo sentimos la opción no es valida")
    print(func())    
  switcher(operaciones)

  while operaciones!='5':
    procesarCheques()


procesarCheques()
