#def gestionar_inventario(inventario_inicial):
 #   inventario=inventario_inicial 
   #print(f"el inventario contiene{inventario} hamburguesas")
  #  print(f"sistema de ventas iniciado")
    
    #while inventario > 0:
     #   if inventario <= 10:
      #      print(f"Advertencia de inventario:solo quedan {inventario} hamburguesas")
       # #simular la venta de una hamburguesas
        #num_hamburguesas=int(input("¿Cuantas hamburguesas quiere el cliente?:"))
        #if num_hamburguesas > inventario:
         #   print("Lo siento, no tenemos suficientes hamburguesas para esa orden.")
        #else:
         #   inventario -= num_hamburguesas
          #  print(f"Se han vendido {num_hamburguesas} hamburguesas. Quedan: {inventario} hamburguesas en el inventario.")
   # print("¡El inventario se ha agotado! No se pueden realizar más ventas.")

#gestionar_inventario(100)


def gestionar_inventario(inventario_inicial):
    inventario = inventario_inicial 
    print(f"sistema de ventas iniciado")
    print(f"el inventario contiene {inventario} hamburguesas")
    
    while inventario > 0:
        if inventario <= 10:
            print(f"Advertencia de inventario: solo quedan {inventario} hamburguesas")
        num_hamburguesas = int(input("¿Cuantas hamburguesas quiere el cliente?: "))
        if num_hamburguesas > inventario:
            print("Lo siento, no tenemos suficientes hamburguesas para esa orden.")
        else:
            inventario -= num_hamburguesas
            print(f"Se han vendido {num_hamburguesas} hamburguesas. Quedan: {inventario} hamburguesas en el inventario.")

    print("¡El inventario se ha agotado! No se pueden realizar más ventas.")
    recarga = input("¿Desea recargar el inventario? (s/n): ")
    if recarga == 's':
        inventario = int(input("¿Cuántas hamburguesas desea añadir?: "))
        gestionar_inventario(inventario)

gestionar_inventario(100)



def gestionar_inventario():
    print("--- 🍔 BIENVENIDO A BURGER-PYTHON 🍔 ---")
    
    while True: # Bucle de recarga (el restaurante sigue abierto)
        inventario = 100
        print(f"\n[SISTEMA] Inventario recargado. Tienes {inventario} hamburguesas listas.")
        
        # Bucle de ventas (mientras haya stock)
        while inventario > 0:
            if inventario <= 10:
                print("🚨 ¡CUIDADO! Solo quedan", inventario, "hamburguesas.")
            try:
                pedido = int(input("\n¿Cuántas hamburguesas quiere el cliente? "))
                
                if pedido < 0:
                    print("❌ Error: No puedes pedir cantidades negativas.")
                elif pedido > inventario:
                    print(f"❌ No tenemos suficiente. Solo quedan {inventario}.")
                else:
                    inventario -= pedido
                    print(f"✅ Venta exitosa. Quedan {inventario} en stock.")
            except ValueError:
                print("❌ Por favor, ingresa un número válido.")
        # Cuando el inventario llega a 0, salimos del bucle interior y venimos aquí:
        print("\n--- 🛑 EL STOCK SE HA AGOTADO ---")
        respuesta = input("¿Deseas recargar el inventario para seguir vendiendo? (si/no): ").lower()
        
        if respuesta != "si":
            print("Cerrando el sistema. ¡Gracias por usar Burger-Python!")
            break # Rompe el bucle exterior y termina el programa
# Llamamos a la función para empezar
gestionar_inventario()
