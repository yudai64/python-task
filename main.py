import math

number = 0
while number <= 360:
  print(str(number)+"°")
  print("sin")
  print(round(math.sin(math.radians(number)), 3))
  print("cos")
  print(round(math.cos(math.radians(number)), 3))
  print("tan")
  if number == 90 or number == 270:
    print("定義できません")
  else:
    print(round(math.tan(math.radians(number)), 3))
  print("\n")
  number += 15