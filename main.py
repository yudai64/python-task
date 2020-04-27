import math

number = 0
while number <= 360:
  print(str(number)+"°")
  print("sin")
  print(math.sin(math.radians(number)))
  print("cos")
  print(math.cos(math.radians(number)))
  print("tan")
  print(math.tan(math.radians(number)))
  print("\n")
  number += 15