# welcome + menu select
print(" Welcome to the Estimated System Avaliability Calculator ")

def menu():
  x=int(input("""\nTo find the estimated system availability, enter 1.
To find the availability of a multiple component system, enter 2.\n"""))

  if x==1:
    estimatedAvailability()
  if x==2:
    multiComponentAvailability()
  else:
    print("invalid")
    

# If you know the mttr and mtbf this calcs the estimated availability 
def estimatedAvailability():
  print("\nRemeber to use seconds as an input")
  mtbf = float(input("Enter MTBF: "))
  print(mtbf)
  mttr = float(input("Enter MTTR): "))
  print (mttr)
  total = mtbf/(mtbf+mttr)*100
  print(total)


# if you know the availaity of a component in % use this to work out availability of multiple components
def multiComponentAvailability():
  compList = []
  total=1
  i=0
  n = int(input("Number of system components: "))
  
  for _ in range(n):
    i=i+1
    compListItem = float(input("Enter availability of component %s: "%i))
    compList.append(compListItem/100)

  for x in compList:
    total *= x

  print(total*100)


#start
menu()

