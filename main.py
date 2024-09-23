"""Ce module permet de retourner une liste de tuple avec leur code ASCII
"""
def artcode_i(s):
    """Retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme itératif.
    
    Args:
    s (str): la chaîne de caractères à encoder
    
    Returns:
    list: la liste des tuples (caractère, nombre d'occurences consécutives)
    """
    t = []  # Liste pour stocker les tuples
    if not s:
        return t

    compteur = 1  # Initialiser le compteur pour le premier caractère
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            compteur += 1  # Incrémenter le compteur si le caractère est le même
        else:
            t.append((s[i - 1], compteur))  # Ajouter le tuple à la liste
            compteur = 1  # Réinitialiser le compteur pour le nouveau caractère

    # Ajouter le dernier caractère et son compteur
    t.append((s[-1], compteur))
    return t  # Retourner la liste de tuples

def artcode_r(s):
    """Retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme récursif. 
    Args: s (str): la chaîne de caractères à encoder 
    Returns: list: la liste des tuples (caractère, nombre d'occurences consécutives)
    """
    if not s:
        return []

    compteur = 1  # Initialiser le compteur pour le premier caractère
    while len(s) > 1 and s[0] == s[1]:
        compteur += 1
        s = s[1:]  # Réduire la chaîne en enlevant le premier caractère
    # Appeler la fonction récursive pour le reste de la chaîne
    return [(s[0], compteur)] + artcode_r(s[compteur:])
    # Utiliser s[compteur:] pour avancer dans la chaîne

def main():
    """Fonction principale pour tester les fonctions d'encodage."""
    print(artcode_i('MMMaaacXolloMM'))
    print(artcode_r('MMMaaacXolloMM'))


if __name__ == "__main__":
    main()
