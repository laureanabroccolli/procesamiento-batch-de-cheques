
from datetime import date, datetime
from pickle import FALSE

class Cheque():
    cheques=[]
    def __init__(self,emisor,monto,fecha=datetime().today()):
        self.emisor=emisor
        self.monto=monto
        self.fecha=fecha
        Cheque.cheques.append(self)
    def __repr__(self):
        return f"   --CHEQUE--: \n*Emisor: {self.emisor} \n*Monto: {self.monto} \n*Fecha de Emision: {self.fecha}"
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
class Usuario(Banco):
    usuarios=[]


    def __init__(self,banco,sucursal,codigoBanco,codigoSucursal,nombre,apellido,dni,fondos,numeroCuenta,categoria):
        super().__init__(banco,sucursal,codigoBanco,codigoSucursal)
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.fondos=int(fondos)
        self.categoria=categoria
        self.numeroCuenta=numeroCuenta
        Usuario.usuarios.append(self)
    def __repr__(self):
        return f"{self.nombre}, {self.apellido},{self.banco},{self.sucursal},{self.dni}\n"
    def buscarSucursal(self,banco):
        for i in Usuario.usuarios:
            if (i.banco==banco):
                print(i.banco)
            
    def crearCheque(self,monto):
        if monto<=self.fondos :
            Cheque(self.nombre,monto,)          
            
        else:
            print('Saldo Insuficiente')

bbva=Banco('BBVA','Catalinas',11000,1)
hsbc=Banco('HSBC','Bouchard',20010,2)
santander=Banco('Santander','Vicente Lopez',49010,23)



usuario1=Usuario(bbva.banco,bbva.sucursal,bbva.codigoBanco,bbva.codigoSucursal,'Tomás','Calabria',31415113,121211,1212121,'Gold')
usuario2=Usuario(hsbc.banco,hsbc.sucursal,hsbc.codigoBanco,hsbc.codigoSucursal,'Juan','Calabria',415623141,31010,2000203,'Gold')
usuario3=Usuario(santander.banco,santander.sucursal,santander.codigoBanco,santander.codigoSucursal,'Angela','Lerena',31049010,93000,3100020,'Standard')


usuario1.crearCheque(400)

usuario1.buscarSucursal('HSBC')
for i in Cheque.cheques:
    print(i)