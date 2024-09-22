todos =["apfel" , "banane"]


for _ in range(1000000000):
  newitem = input("Was möchtest du hinzufügen? ")
  todos.append(newitem)
  print("Elemente:")

  for todo in todos:
   print(f"- {todo}")