# 18.10.24
# Ülesanne 6

import turtle
import math

kordaja = 10
a = math.radians(53)
h = 10
x = abs(h / math.tan(a))
c = math.sqrt(h**2 + x**2)

print(x)

turtle.fd(x*kordaja)
turtle.lt(90)
turtle.fd(h*kordaja)
turtle.lt(180-(180-90-53))
turtle.fd(14*kordaja)






turtle.done

