import math

r = 0
while r <= 360:
  print(str(r)+"°")
  print("sin" + str(r) + "°= " + str(math.sin(math.radians(r))))
  print("cos" + str(r) + "°= " + str(math.cos(math.radians(r))))
  print("tan" +str(r) + "°= " + str(math.tan(math.radians(r))))
  print("\n")
  r += 15