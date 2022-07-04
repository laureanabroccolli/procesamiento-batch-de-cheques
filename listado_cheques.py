import csv

cheques = list()

with open('Clientes.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    cheques.append(row)
    print("DNI: {0}, Tipo: {1}, Estado: {2}, FechaOrigen: {3}, FechaPago: {4}".format(row[8],row[10],row[9],row[6],row[7]))

# Modificar lo anterior