import re

def validar_nom(nom):
    """Valida que el nom només contingui lletres i espais"""
    return bool(re.match(r'^[a-zA-ZÀ-ÿ\s]{2,}$', nom))  # Mínimo 2 caracteres