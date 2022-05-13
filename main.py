from queries import selectcep

cep = input("Insert a Cep: ")
result = selectcep(cep)
if result:
  print(result)
else:
  print("Something went wrong!")
