#frutas = { "manzanas": 10, "bananas": 5 }#inicializamos el diccionario con dos cajas 
#frutas["bananas"] = 13 #actualizamos el valor de la caja de bananas a 13
#frutas["naranjas"] = 7 #agregamos una nuevo tipo de fruta, una nueva caja que tiene 7 naranjas 

#total_frutas = sum(frutas.values()) #sumamos el numero de frutas que tenemos en total utilizando el metodo values() del diccionario

#print(frutas) #imprimimos el diccionario completo

#print(f"Tenemos {frutas['manzanas']} manzanas en la caja") #imprimimos el numero de frutas que tenemos en cada caja utilizando las claves del diccionario

#print(f"Tenemos un total de {total_frutas} frutas en todas las cajas") #imprimimos el total de frutas que tenemos en todas las cajas utilizando la variable total_frutas que calculamos anteriormente


#fusionar dos diccionarios utilizando el metodo update() del diccionario

#datos_basicos = {"nombre": "gamerx", "nivel": 15}

#datos_extra= {"puntos": 2500, "nivel": 16}

#datos_perfil= datos_basicos.copy() #creamos una copia del diccionario datos_basicos para no modificarlo directamente

#datos_perfil.update(datos_extra) #fusionamos los dos diccionarios utilizando el metodo update() del diccionario

#print(datos_perfil) #imprimimos el diccionario fusionado que contiene toda la informacion del perfil del jugador


#creamos la ficha tecnica de un influencer utilizando un diccionario

campaña_verano = { 
    "cliente":"supersoda",
    "presupuesto": 50000,
    "reddes" : ["instagram", "tiktok",],
    "objetivo_kpi": "aumentar seguidores",
    "finalizada": False
}

#pedimos los datos del cliente usando las claves del diccionario para mostrar la informacion de la campaña
print(f"Campaña para el cliente: {campaña_verano['cliente']}")

#actualizamos el presupuesto de la campaña 
campaña_verano["presupuesto"] = 60000

campaña_verano["responsable"] = "sara"

#actualializacion de la camapaña 

print(f"actualizacion de la campaña: {campaña_verano}")
