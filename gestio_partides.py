import random
from itertools import combinations

def generar_partides(participants):
    """Genera partides aleatòries entre participants"""
    partides = []
    # Generar todos los posibles emparejamientos
    emparejamientos = list(combinations(participants, 2))
    random.shuffle(emparejamientos)
    
    # Crear partidas (en una aplicación real tendríamos más detalles)
    for jugador1, jugador2 in emparejamientos:
        partides.append({
            'jugador1': jugador1,
            'jugador2': jugador2,
            'resultat': None  # Pendiente de jugar
        })
    return partides

def desar_partides_a_fitxer(partides, fitxer):
    """Desa les partides en un fitxer"""
    with open(fitxer, 'w') as f:
        for partida in partides:
            linea = f"{partida['jugador1']},{partida['jugador2']},{partida.get('resultat', '')}\n"
            f.write(linea)

def carregar_partides_de_fitxer(fitxer):
    """Carrega les partides des d'un fitxer"""
    partides = []
    try:
        with open(fitxer, 'r') as f:
            for line in f:
                jugador1, jugador2, resultat = line.strip().split(',')
                partida = {
                    'jugador1': jugador1,
                    'jugador2': jugador2,
                    'resultat': resultat if resultat else None
                }
                partides.append(partida)
    except FileNotFoundError:
        pass
    return partides