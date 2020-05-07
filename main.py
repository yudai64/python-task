import math

angle = 0
while angle <= 360:
  print(str(angle)+"°")
  print("sin" + str(angle) + "°= " + str(math.sin(math.radians(angle))))
  print("cos" + str(angle) + "°= " + str(math.cos(math.radians(angle))))
  print("tan" +str(angle) + "°= " + str(math.tan(math.radians(angle))))
  print("\n")
  angle += 15