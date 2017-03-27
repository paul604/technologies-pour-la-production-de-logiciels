
'''
Met à disposition un service web de récupération de de données en JSON à l'aide de la librairie bottle.
http://bottlepy.org/docs/dev/tutorial.html
'''


import json
from config import PROJECT_ROOT
from ..lib.bottle import route, run
from ...database.dao.dao.dao_installation import *
from ...database.dao.dao.dao_equipement import *
from ...database.dao.dao.dao_activite import *



def launch_rest_api_service(host='localhost', port=1234, debug=False):
	'''
	Permet le lancement du serveur bottle
	'''
	run(host=host, port=port, debug=debug)



# ---------------------------------------------- Définition des routes dynamiques : accès aux données en fonction de la structure de l'URL
'''
i_id   identifiant d'une installation
e_id   identifiant d'un équipement
a_id   identifiant d'une activité

------

Exemple de la forme du JSON final (node data)

{
	"data":[
		{"id":"id1","nom":"nom1","adresse":"adresse1","code_postal":"code_postal1","ville":"ville1"},
		{"id":"id2","nom":"nom2","adresse":"adresse2","code_postal":"code_postal2","ville":"ville2"},
		{"id":"id3","nom":"nom3","adresse":"adresse3","code_postal":"code_postal3","ville":"ville3"}
	]
}
'''

# toutes les installations
@route('/data/installations')
def get_i():
	return '{"data":['+','.join([json.dumps(o.__dict__, ensure_ascii=False) for o in db2object()])+']}'


# une installation
@route('/data/installations/<i_id:int>')
def get_i(i_id):
	return None #TODO
 




