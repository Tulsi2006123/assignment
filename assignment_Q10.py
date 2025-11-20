num=int(input("Enter number of people:"))
skillsneed=int(input("Enter number of skills needed:"))
for i in range(num):
    skills=int(input("people have skills:"))
    if skills>=skillsneed:
      print("Yes")
    else:
      print("No")