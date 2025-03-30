def afegir_participant(nom, participants):
    """Afegeix un nou participant a la llista si no existeix"""
    if nom not in participants:
        participants.append(nom)
    return participants

def desar_participants_a_fitxer(participants, fitxer):
    """Desa la llista de participants en un fitxer"""
    with open(fitxer, 'w', encoding='utf-8') as f:
        for participant in participants:
            f.write(f"{participant}\n")

def carregar_participants_de_fitxer(fitxer):
    """Carrega la llista de participants des d'un fitxer"""
    participants = []
    try:
        with open(fitxer, 'r', encoding='utf-8') as f:
            participants = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        pass
    return participants