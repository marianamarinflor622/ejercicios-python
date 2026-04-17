# 1. Lista con 3 diccionarios (influencers)
influencers = [
    {"nombre": "Carlos García",   "seguidores": 150000, "tematica": "Gaming"},
    {"nombre": "Lucía Martínez",  "seguidores": 230000, "tematica": "Moda"},
    {"nombre": "Raúl Fernández",  "seguidores": 98000,  "tematica": "Cocina"}
]

# 2. Añadir un 4º influencer con .append()
influencers.append(
    {"nombre": "Sara López", "seguidores": 310000, "tematica": "Viajes"}
)

# 3. Imprimir el nombre del SEGUNDO influencer (índice 1)
print(influencers[1]["nombre"])
#lucia martinez


print(f"Lista completa de influencers: {influencers}")
#comprobamos que se se añadiera sala lopez 