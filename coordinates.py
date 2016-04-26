import math

def coordinates(deg, radius):
	rad = math.radians(deg)
	x= radius * math.cos(rad)
	y= radius * math.sin(rad)
	return (round(x,10), round(y,10))


print coordinates(45,1)
print coordinates(90,1)