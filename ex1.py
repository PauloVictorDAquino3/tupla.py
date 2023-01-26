lanches= ["hamburguer", "pizza", "Refri", "bala"] 
 
while lanches:
  opcao=str(input("Qual você escolhe? {hamburguer, pizza, Refri, bala} "))
  if opcao == "hamburguer":
    print (f"Receba seu {lanches [0]}")
  elif opcao == "pizza":
    print (f"Receba sua {lanches [1]}")
  elif opcao == "refri":
    print (f"Receba seu {lanches [2]}")
  elif opcao == "bala":
    print (f"Receba sua {lanches [3]}")
  else:
    print ("Por favor faça um pedido de acordo com o cardápio.")
