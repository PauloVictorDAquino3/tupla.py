num = [
  "zero", "um", "dois", "três", "quatro", "cinco", "seis",
  "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
  "dezesseis", "dezesete", "dezoito", "dezenove", "vinte"
]
escolha = int(input("Escolha um numero de 0 a 20: "))

while True:
  if escolha >=0 or escolha <= 20:
    break
while escolha <0 or escolha >20:
  print ("tente novamente")
  break
print(f"o numero de um a vinte escolhido foi: { num [escolha]}")
