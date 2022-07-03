
# Falta:
#  agregar funcion para agregar Usuarios por consola
#  agregar funcion para agregar cheques por consola
#  Agregar funcion para buscar Usuarios y cheques por consola


import csv
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
        return f"{self.banco},{self.sucursal},{self.codigoBanco},{self.codigoSucursal},{self.nombre},{self.apellido},{self.dni},{self.fondos},{self.numeroCuenta}"
   
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



print(Cheque.cheques)


Usuario.crearUsuarioConCSV()
Usuario.crearChequeConCSV(Usuario.usuarios)

