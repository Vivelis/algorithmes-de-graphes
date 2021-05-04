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



def plus_court_chemin(G, s, d):
	"""entrée : G = liste d'adjacence; s = sommet de départ; d = sommet d'arrivée
        retourne : Liste de sommets correspondant au trajet entre s et d"""
    prédecesseurs = {s: None}    # dictionnaire des prédecesseurs
    f = []    # f = CreerFile();
    f.append(s)    # f.enfiler(s);
    marqués = [s]    # marquer(s);
    while f:    # TANT QUE la file est non vide
        s = f.pop(-1)    # On récupère le noeud
        for t in G[s]:    # POUR TOUT voisin t de s dans G
            if t == d:
                ville = s    # Destination trouvée, on remonte le chemin
                chemin = [d]
                while ville:
                    chemin.append(ville)
                    ville = prédecesseurs[ville]
                chemin.reverse()    # On remet dans l'ordre
                return chemin
            elif t not in marqués:    # SI t non marqué
                f.append(t)    # f.enfiler(t);
                marqués.append(t)    # marquer(t);
                prédecesseurs[t] = s    # màJ du dictionnaire de prédecesseurs 
    return []# Destination non trouvée  
                
print("Chemin le plus court")
print("---------------------------------------")
print(plus_court_chemin(dg,"Nice","Toulouse"))
print("-----------------------------------")
