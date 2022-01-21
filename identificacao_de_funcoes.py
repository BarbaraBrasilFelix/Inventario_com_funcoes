inventario=[]

def preencherInventario (inventario):
  resp="S"
  while resp == "S":
    equipamento = [input("Equipamento: "),
                 float(input("Valor: ")),
                 int(input("Número Serial: ")),
                 input("Departamento: ")]
    inventario.append(equipamento)
    resp = input("Digite 'S' para incluir mais itens: ").upper()

def exibirInventario(inventario):
  for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

def localizarPorNome(inventario):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in inventario:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

def excluirPorSerial(inventario):
  serial=int(input("Digite o serial do equipamento que será excluido: "))
  for elemento in inventario:
    if elemento[2]==serial:
      inventario.remove(elemento)
  return "Itens excluídos se estavam na lista."

