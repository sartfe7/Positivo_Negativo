# Programa para verificar si un numero es positivo o negativo

# Input
X = int(input("digite un numero: "))

# Processing
if X > 0:
    RTA = "Positivo"
elif X == 0:
    RTA = "su numero es neutro "
else:
    RTA = "negativo"

# Output
print("el numero",X,"es",RTA)