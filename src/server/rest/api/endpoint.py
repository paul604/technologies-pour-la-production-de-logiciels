
'''
Met à disposition un service web de récupération de de données en JSON à l'aide de la librairie bottle.
http://bottlepy.org/docs/dev/tutorial.html
'''



from rest.lib.bottle import route, run
from ...database.dao.bean import * #FIXME ValueError: attempted relative import beyond top-level package



def launch_rest_api_service(host='localhost', port=1234, debug=False):
	'''
	Permet le lancement du serveur bottle
	'''
	run(host=host, port=port, debug=debug)



# ---------------------------------------------- Définition des routes dynamiques : accès aux données en fonction de la structure de l'URL
# i_id   identifiant d'une installation
# e_id   identifiant d'un équipement
# a_id   identifiant d'une activité


# toutes les installations
@route('/data')
def get_i():
	return None #TODO 


# une installation
@route('/data/<i_id:int>')
def get_i(id):
	return None #TODO 
