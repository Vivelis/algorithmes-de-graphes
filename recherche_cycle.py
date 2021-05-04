dg = {'Paris': ['Lyon', 'Toulouse', 'Rennes', 'Nancy'], 'Lyon': ['Paris', 'Marseille', 'Nice', 'Nancy'], 'Marseille': ['Lyon', 'Nice', 'Montpellier'], 'Nice': ['Marseille', 'Lyon'], 'Montpellier': ['Marseille', 'Toulouse'], 'Toulouse': ['Montpellier', 'Paris', 'Rennes'], 'Rennes': ['Toulouse', 'Paris'], 'Nancy': ['Paris', 'Lyon']}

def recherche_cycle(G, s, vus=None):
    """entrée : G = liste d'adjacence; s = sommet de départ
        vus = liste des sommets visités
        retourne : True = Il y a un cycle; False = Il n'y a pas de cycle"""
    if vus is None:
        vus = []
    voisins = G[s]		# on récupère la liste des voisins
    vus.append(s)		# marquer le sommet s
    for t in voisins:	# POUR TOUT sommet t voisin du sommet s
        if t in vus:
            return True
        else:    		# SI t n'est pas marqué ALORS
            recherche_cycle(G, t, vus)
    return False

print("Présence d'un cycle")
print("-------------------")
print(recherche_cycle(dg, "Nice"))
print(  "----------------------------")
