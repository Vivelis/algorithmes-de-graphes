Graphe_villes = {'Paris': ['Lyon', 'Toulouse', 'Rennes', 'Nancy'], 'Lyon': ['Paris', 'Marseille', 'Nice', 'Nancy'], 'Marseille': ['Lyon', 'Nice', 'Montpellier'], 'Nice': ['Marseille', 'Lyon'], 'Montpellier': ['Marseille', 'Toulouse'], 'Toulouse': ['Montpellier', 'Paris', 'Rennes'], 'Rennes': ['Toulouse', 'Paris'], 'Nancy': ['Paris', 'Lyon']}

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
print(plus_court_chemin(Graphe_villes,"Nice","Toulouse"))
print("-----------------------------------")

def recherche_chemin(Graphe, depart, arrivee,Vus = None):
	"""entrée : Graphe = liste d'adjacence, depart = sommet de départ, arrivee = sommet d'arrivée
		retourne : Liste de sommets correspondant au chemin entre depart et arrivee"""
	assert depart in Graphe and arrivee in Graphe, "un sommet donné n'appartient pas au graphe"
	if Vus is None:		# initialise liste sommets vus
		Vus = []
	voisins = Graphe[depart]		# on récupère la liste des voisins
	Vus.append(depart)				# marquer le sommet depart
	for t in voisins:				# POUR TOUT sommet t voisin du sommet depart
		if t == arrivee:			# cas où l'on trouve l'arrivée
			Vus.append(t)
			return Vus
		elif t not in Vus :    		# SI t n'est pas marqué ALORS
			return recherche_chemin(Graphe,t,arrivee,Vus)
	return False

print("Chemin")
print("---------------------------------------")
print(recherche_chemin(Graphe_villes,"Nice","Toulouse"))
print("-----------------------------------")


def recherche_tous_chemins(Graphe, depart, arrivee)
	"""entrée : Graphe = liste d'adjacence, depart = sommet de départ, arrivee = sommet d'arrivée
		retourne : Liste de liste de sommets correspondant aux chemin entre depart et arrivee"""
	for i in Graphe:
		recherche_chemin(Graphe,depart,arrivee,Vus=[i])