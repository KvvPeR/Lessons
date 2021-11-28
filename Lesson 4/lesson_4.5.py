import math
a = float(input('vvedite storonu triugolnika'))
radius = float(input('vvedite radius triugolnika'))
if radius == a * math.sqrt(3)/6:
    print('mojno')
else:
    print('nelzya')