from identificacao_de_funcoes import *

minhaLista=[]
print("=====Preenchendo=====")
preencherInventario(minhaLista)

print("\n=====Exibindo=====")
exibirInventario(minhaLista)

print("\n=====Pesquisando=====")
localizarPorNome(minhaLista)

print("\n=====Excluindo=====")
print(excluirPorSerial(minhaLista))

print("\n=====Exibindo=====")
exibirInventario(minhaLista)
