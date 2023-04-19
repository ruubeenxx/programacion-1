#Diccionario con la información de los vuelos
vuelos = {
    "1": {
        "origen": "aguachica",
        "destino": "Medellín",
        "hora": "8:30 AM",
        "precio": 250000,
        "tipo": "Nacional",
        "avion": "Boeing 737",
        "matricula": "HK-54321",
        "puerta_abordaje": "A4",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "Avianca"
    },
    "2": {
        "origen": "aguachica",
        "destino": "Miami",
        "hora": "2:00 PM",
        "precio": 800000,
        "tipo": "Internacional",
        "avion": "Airbus A320",
        "matricula": "N12345",
        "puerta_abordaje": "B6",
        "sillas_disponibles": 200,
        "sillas_asignadas": [],
        "aerolinea" : "Avianca"
    },
    "3": {
        "origen": "aguachica",
        "destino": "Medellín",
        "hora": "8:30 AM",
        "precio": 250000,
        "tipo": "Nacional",
        "avion": "Boeing 737",
        "matricula": "HK-54321",
        "puerta_abordaje": "A4",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "LATAM"
    },
    "4": {
        "origen": "aguachica",
        "destino": "cali",
        "hora": "5:30 AM",
        "precio": 270000,
        "tipo": "Nacional",
        "avion": "Boeing 787",
        "matricula": "HK-5456221",
        "puerta_abordaje": "S3",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "VIVA AIR"
    },
    "5": {
        "origen": "aguachica",
        "destino": "cucuta",
        "hora": "7:30 AM",
        "precio": 240000,
        "tipo": "Nacional",
        "avion": "Boeing 777",
        "matricula": "HK-00984321",
        "puerta_abordaje": "B2",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "WINGO"
    },
    "6": {
        "origen": "aguachica",
        "destino": "santa marta",
        "hora": "11:30 AM",
        "precio": 250000,
        "tipo": "Nacional",
        "avion": "Boeing 737 max",
        "matricula": "FK-54321",
        "puerta_abordaje": "A34",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "EASYFLY"
    },
    "7": {
        "origen": "aguachica",
        "destino": "gamarra",
        "hora": "8:10 AM",
        "precio": 25000,
        "tipo": "Nacional",
        "avion": "Boeing 737",
        "matricula": "HK-5497621",
        "puerta_abordaje": "A2",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "ULTRA"
    },
    "8": {
        "origen": "aguachica",
        "destino": "brasil",
        "hora": "10:30 AM",
        "precio": 2500000,
        "tipo": "internacional",
        "avion": "Boeing 777",
        "matricula": "HK-587321",
        "puerta_abordaje": "A1",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "AVIANCA EXPRESS"
    },
    "9": {
        "origen": "aguachica",
        "destino": "mexico",
        "hora": "8:30 PM",
        "precio": 1200000,
        "tipo": "internacional",
        "avion": "Boeing 767",
        "matricula": "HK-54921",
        "puerta_abordaje": "A9",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "Avianca"
    },
    "10": {
        "origen": "aguachica",
        "destino": "caracas",
        "hora": "8:00 PM",
        "precio": 1500000,
        "tipo": "internacional",
        "avion": "Boeing 747",
        "matricula": "HK-54381",
        "puerta_abordaje": "AD",
        "sillas_disponibles": 100,
        "sillas_asignadas": [],
        "aerolinea" : "SATENA"
    }
    
}

# Solicitar al usuario seleccionar un vuelo
print("Seleccione un vuelo:")
for key, vuelo in vuelos.items():
    print(
        f"{key}. Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Hora: {vuelo['hora']}, Precio: ${vuelo['precio']}, Tipo: {vuelo['tipo']}, aerolinea: {vuelo['aerolinea']}"
    )

vuelo_elegido = input("Ingrese el número de vuelo elegido: ")

# Validar entrada del usuario
while vuelo_elegido not in vuelos.keys():
    print("Opción inválida. Por favor, ingrese un número de vuelo válido.")
    vuelo_elegido = input("Ingrese el número de vuelo elegido: ")

# Solicitar información del pasajero
nombre = input("Ingrese su nombre y apellido completo: ")
cedula = input("Ingrese su número de cédula: ")
telefono = input("Ingrese su número de teléfono: ")


# Asignar silla al pasajero
vuelo = vuelos[vuelo_elegido]
silla_asignada = None
if vuelo["sillas_disponibles"] > 0:
    silla_asignada = vuelo["sillas_disponibles"]
    vuelo["sillas_disponibles"] -= 1
    vuelo["sillas_asignadas"].append(silla_asignada)

# Generar ticket de vuelo
ticket = {
    "Origen": vuelo["origen"],
    "Destino": vuelo["destino"],
    "Hora": vuelo["hora"],
    "Precio": vuelo["precio"],
    "aerolinea":vuelo["aerolinea"],
    "Tipo": vuelo["tipo"],
    "Avion": vuelo["avion"],
    "Matricula": vuelo["matricula"],
    "Puerta de Abordaje": vuelo["puerta_abordaje"],
    "Silla": silla_asignada,
    "Nombre": nombre,
    "Cedula": cedula,
    "Telefono": telefono,
}

# Imprimir ticket de vuelo
print("\n--- TICKET DE VUELO ---")
print("--------------------------")
print("PASE DE ABORDAR/BOARDING PASS")
print("------------------------------")
for key, value in ticket.items():
    print(f"{key}: {value}")
print("-------------------------------")
print("OPERADO POR/OPERATED BY RUBEN JEJEJE")


