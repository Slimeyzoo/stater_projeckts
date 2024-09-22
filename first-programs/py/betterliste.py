todos =[]

for _ in range(1000000000):

 print("was wilst du tuen")
 print("1 todus anzeigen.")
 print("2 todus hinzufügen.")
  
 optionen = input("1 oder 2? ")

 if int(optionen) == 1: 
  print("Elemente:")

  for todo in todos:
   print(f"- {todo}")


 if int(optionen) == 2: 
   newitem = input("Was möchtest du hinzufügen? ")
   todos.append(newitem) 
 

 if int(optionen) == 3:
     exit()

