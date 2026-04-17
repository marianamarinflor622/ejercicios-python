#invitados = ["shakira", "coldplay", "beyonce", "stromae", "camillo", "lady gaga"]
#invitados.append("bruno mars") #agrega un nuevo invitado al final de la lista respetando el orden 
#invitados.remove("beyonce") #elimina un invitado de la lista y la posicion de ella la ocupa la persona que esta adelante 
#invitados_totales = len(invitados) #cuenta el numero de invitados que hay en la lista
#invitados.sort() #ordena la lista de invitados alfabeticamente

#print(f"la lista final para la fiesta es : {invitados}")

#print(f"total de acreditaciones:{invitados_totales}")




#sumamar precios de una lista 

#precios=[120,200,150,300,250]
#total = sum(precios) #suma todos los precios de la lista
#print(f"el total de los precios es: {total}€")

colores = ["rojo", "azul", "verde","rojo", "amarillo","rojo", "morado"]
colores.insert(2,"naranja") #agrega un nuevo color en la posicion 2 y el resto de los colores se desplazan una posicion hacia adelante
total_rojo= colores.count("rojo") #cuenta cuantas veces se repite el color rojo en la lista

print(colores)
print("colores")
print(f"el color rojo se repite {total_rojo} veces en la lista")