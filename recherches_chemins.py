dg = {'Paris': ['Lyon', 'Toulouse', 'Rennes', 'Nancy'], 'Lyon': ['Paris', 'Marseille', 'Nice', 'Nancy'], 'Marseille': ['Lyon', 'Nice', 'Montpellier'], 'Nice': ['Marseille', 'Lyon'], 'Montpellier': ['Marseille', 'Toulouse'], 'Toulouse': ['Montpellier', 'Paris', 'Rennes'], 'Rennes': ['Toulouse', 'Paris'], 'Nancy': ['Paris', 'Lyon']}

def plus_court_chemin(Graphe, depart, arrivee):
	"""entrée : Graphe = liste d'adjacence; depart = sommet de départ; arrivee = sommet d'arrivée
        retourne : Liste de sommets correspondant au trajet entre depart et arrivee"""
    prédecesseurs = {depart: None}    # dictionnaire des prédecesseurs
    f = []    # f = CreerFile();
    f.append(depart)    # f.enfiler(depart);
    marqués = [depart]    # marquer(depart);
    while f:    # TANT QUE la file est non vide
        depart = f.pop(-1)    # On récupère le noeud
        for t in Graphe[depart]:    # POUR TOUT voisin t de depart dans Graphe
            if t == arrivee:
                ville = depart    # Destination trouvée, on remonte le chemin
                chemin = [arrivee]
                while ville:
                    chemin.append(ville)
                    ville = prédecesseurs[ville]
                chemin.reverse()    # On remet dans l'ordre
                return chemin
            elif t not in marqués:    # SI t non marqué
                f.append(t)    # f.enfiler(t);
                marqués.append(t)    # marquer(t);
                prédecesseurs[t] = depart    # màJ du dictionnaire de prédecesseurs 
    return []# Destination non trouvée  
                
print("Chemin le plus court")
print("---------------------------------------")
print(plus_court_chemin(dg,"Nice","Toulouse"))
print("-----------------------------------")

def recherche_chemin(Graphe, depart, arrivee):
	"""entrée : Graphe = liste d'adjacence, depart = sommet de départ, arrivee = sommet d'arrivée
		retourne : Liste de sommets correspondant au chemin entre depart et arrivee"""