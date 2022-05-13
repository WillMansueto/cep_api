from queries import select_cep

cep = input("Insert a Cep: ")
result = select_cep(cep)
if result:
  print(result)
else:
  print("Something went wrong!")
