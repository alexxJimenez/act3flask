def actualitzar_puntuacions(puntuacions, guanyador):
    """Actualitza les puntuacions quan hi ha un guanyador"""
    if guanyador in puntuacions:
        puntuacions[guanyador] += 1
    return puntuacions

def calcular_ranquing(puntuacions):
    """Calcula el rànquing ordenat per puntuació"""
    return sorted(puntuacions.items(), key=lambda item: item[1], reverse=True)