# Falta:
#  agregar funcion para agregar Usuarios por consola
#  agregar funcion para agregar cheques por consola
#  Agregar funcion para buscar Usuarios y cheques por consola


import csv
from Cheque import *
cheques = list()

with open('Clientes.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    nuevo_cheque = Cheque('??', row[6], row[7])
    cheques.append(nuevo_cheque)
    print("DNI: {0}, Tipo: {1}, Estado: {2}, FechaOrigen: {3}, FechaPago: {4}".format(row[8],row[10],row[9],row[6],row[7]))

print(cheques)

class Cheque():
    cheques=[]
    def __init__(self,numeroCuenta,cuentaDestino,valor,fechaEmision,fechaPago,tipo,estado,dni):
        self.numeroCuenta=numeroCuenta
        self.cuentaDestino=cuentaDestino
        self.valor=valor
        self.fechaEmision=fechaEmision
        self.fechaPago=fechaPago,
        self.tipo=tipo,
        self.dni=dni
        self.estado=estado
        Cheque.cheques.append(self)
    def __repr__(self):
        return f"   --CHEQUE--: \n*Emisor: {self.numeroCuenta} \n*Monto: {self.valor} \n*Fecha de Emision: {self.fechaEmision} \n*Destinatario:{self.cuentaDestino} \n*Fecha de Emision:{self.fechaPago} \n*Estado:{self.estado}\n dni:{self.dni}\n"

class Banco():
    bancos=[]
    def __init__(self,banco,sucursal,codigoBanco,codigoSucursal):
        self.banco=banco
        self.sucursal=sucursal
        self.codigoBanco=codigoBanco
        self.codigoSucursal=codigoSucursal
        Banco.bancos.append(self)
    def __repr__(self):
        return f"Banco:{self.banco}, Sucursal:{self.sucursal}, codigoBanco:{self.codigoBanco}, CodigoSucursal:{self.codigoSucursal}\n"
class Usuario(Banco,Cheque):
    usuarios=[]

    def __init__(self,banco,sucursal,codigoBanco,codigoSucursal,nombre,apellido,dni,fondos,numeroCuenta):
        super().__init__(banco,sucursal,codigoBanco,codigoSucursal)
        
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.fondos=fondos
        self.numeroCuenta=numeroCuenta
        Usuario.usuarios.append(self)
    def __repr__(self):
        return f"\nBanco:  {self.banco},\nSucursal:  {self.sucursal},\nCodigoBanco:  {self.codigoBanco},\nCodigoSucursal:  {self.codigoSucursal},\nNombre:  {self.nombre},\nApellido:  {self.apellido},\nDNI:  {self.dni},\nFondos: $ {self.fondos},\nN° de Cuenta:  {self.numeroCuenta}"
   
    def crearUsuarioConCSV():
        with open(r'Clientes.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader :
                Usuario(row[3],row[4],row[5],row[6],row[0],row[1],row[13],int(row[12]),row[8])

                Cheque(row[8],row[7],row[9],row[10],row[11],row[15],row[14],row[13])
    def crearChequeConCSV(self):
          with open(r'Clientes.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader :
                if(row[12]<=row[9]):
                    Cheque(row[8],row[7],int(row[9]),row[10],row[11],row[15],row[14],row[13])
                else:
                 print(f"Lo sentimos {row[0]},no posees saldo suficiente para librar este cheque")
    def buscarChequesPorUsuario():
        dni=input('ingrese su numero de dni:\n----> ')
        for i in Cheque.cheques:
            if dni==i.dni:
                print(f"Ingresaste los siguientes cheques: \n {i}")
            else: 
                print('Lo sentimos no poseemos cheques que concuerden con la información ingresada')
    
    def buscarDatosPorConsola():
        dni=input('ingrese su numero de dni:\n----> ')
        for i in Usuario.usuarios:
           if (i.dni==dni):
                print(f"{i}\n\n")


Usuario.crearUsuarioConCSV()
Usuario.crearChequeConCSV(Usuario.usuarios)
# Usuario.buscarChequesPorUsuario()
Usuario.buscarDatosPorConsola()

