import csv

with open('Clientes.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    print("DNI: {8}, Tipo: {10}, Estado: {9}, FechaOrigen: {6}, FechaPago: {7}".format(row[8],row[10],row[9],row[6],row[7]))

# Modificar lo anterior