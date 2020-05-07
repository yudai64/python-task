import math

angle = 0
while angle <= 360:
  print(str(angle)+"°")
  print("sin" + str(angle) + "°= " + str(round(math.sin(math.radians(angle)), 3)))
  # print(round(math.sin(math.radians(angle)), 3))
  print("cos" + str(angle) + "°= " + str(round(math.cos(math.radians(angle)), 3)))
  print("tan" +str(angle) + "°= " + str(round(math.tan(math.radians(angle)), 3)))
  # print(round(math.tan(math.radians(angle)), 3))
  print("\n")
  angle += 15