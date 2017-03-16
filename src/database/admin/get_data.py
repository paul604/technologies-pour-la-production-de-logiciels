

'''
Fournit un ensemble de fonction pour :
	* télécharger les fichiers CSV contenant les données
	* les parser pour en insérer les données dans une base SQLite
'''

import os, urllib.request
import csv

def dl_data(where_to_put_data, override = False):
	'''
	Le paramètre override permet d'activer ou non l'écrasement des CSV.
	Activer pour les télécharger à nouveau les CVS même si les fichiers existent.
	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists(where_to_put_data+'/data'):
		os.mkdir(where_to_put_data+'/data');

	if not os.path.exists(where_to_put_data+'/data/csv'):
		os.mkdir(where_to_put_data+'/data/csv');

	# on y télécharge les CSV
	if override or not os.path.isfile(where_to_put_data+'/data/csv/installations.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv', where_to_put_data+'/data/csv/installations.csv')
	if override or not os.path.isfile(where_to_put_data+'/data/csv/equipements.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv', where_to_put_data+'/data/csv/equipements.csv')
	if override or not os.path.isfile(where_to_put_data+'/data/csv/activites.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv', where_to_put_data+'/data/csv/activites.csv')