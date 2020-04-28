import math

angle = 0
while angle <= 360:
  print(str(angle)+"°")
  print("sin")
  if angle == 0 or angle == 180 or angle == 360:
    print(0)
  else:
    print(round(math.sin(math.radians(angle)), 3))
  print("cos")
  if angle == 90 or angle == 270:
    print(0)
  else:
    print(round(math.cos(math.radians(angle)), 3))
  print("tan")
  if angle == 90 or angle == 270:
    print("定義できません")
  elif angle == 0 or angle == 180 or angle == 360:
    print(0)
  else:
    print(round(math.tan(math.radians(angle)), 3))
  print("\n")
  angle += 15