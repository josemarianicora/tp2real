# Procesar cada ronda
def calcular_puntaje(kills, assists, deaths):
    return (kills * 3) + assists - (1 if deaths else 0)
