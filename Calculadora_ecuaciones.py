#cabecera

print(""" 
..######.....###....##........######..##.....##.##..........###....########...#######..########.....###......
.##....##...##.##...##.......##....##.##.....##.##.........##.##...##.....##.##.....##.##.....##...##.##.....
.##........##...##..##.......##.......##.....##.##........##...##..##.....##.##.....##.##.....##..##...##....
.##.......##.....##.##.......##.......##.....##.##.......##.....##.##.....##.##.....##.########..##.....##...
.##.......#########.##.......##.......##.....##.##.......#########.##.....##.##.....##.##...##...#########...
.##....##.##.....##.##.......##....##.##.....##.##.......##.....##.##.....##.##.....##.##....##..##.....##...
..######..##.....##.########..######...#######..########.##.....##.########...#######..##.....##.##.....##...
 """)
print("Author: @klacode")
print("\ncalculadora de la forma Ax^2+Bx+C con números enteros")
#Meter datos
print("\nPon A:") 
num_a=input()

print("Pon B:")
num_b=input()

print("Pon C:")
num_c=input()
#convierte los numeros en entidades enteras
numm_a=int(num_a)
numm_b=int(num_b)
numm_c=int(num_c)
#Si la ecuacion no tiene solución 
if numm_b**2-4*numm_a*numm_c<0 :
	print("no tiene solución") 
#Si la ecuacion tiene solucion hace las operaciones
else:
	print("\nSOLUCIONES")
	import math
	print((-numm_b+math.sqrt(numm_b**2-4*numm_a*numm_c))/(2*numm_a))
	print((-numm_b-math.sqrt(numm_b**2-4*numm_a*numm_c))/(2*numm_a))


