nombre = str(input("Intruduce tu nombre: "))
print(f"¡Hola, {nombre}!")
total_compras_anuales = float(input("introduce total de compras anuales: "))
if(total_compras_anuales<5000):
    print("Cliente básico")
elif(total_compras_anuales<=5000):
    print("Cliente regular")
elif(total_compras_anuales>=20000):
    print("Cliente premium")
elif(total_compras_anuales>=50000):
    print("ClienteVIP")