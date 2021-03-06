import sqlite3
from config import DB_FULLPATH, printex
from ..bean.Activite import Activite



def a_get_object_by_id(a_id = -1):
    '''
    Retourne l'activite avec l'id passé en param ou si id == -1 retourne l'ensemble des activites contenus dans la base de données sous forme d'objets Activite
    '''
    activites = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()

        if(a_id == -1): # toutes
            cur.execute("""SELECT a.id, a.nom, a.numero_activites, a.numero_equipements, a.desc_act FROM activite a""")
        else: # via id
            cur.execute("""SELECT a.id, a.nom, a.numero_activites, a.numero_equipements, a.desc_act FROM activite a WHERE a.id=?""", [a_id])

        rows = cur.fetchall()
        for row in rows:
            activites.add(Activite(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return activites



def a_get_object_by_num_act(num_act):
    '''
    Retourne l'ensemble des activitées ayant le num_act == numero_activite
    '''
    activites = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT a.id, a.nom, a.numero_activites, a.numero_equipements, a.desc_act FROM activite a WHERE a.numero_activites=?""", [num_act])
        rows = cur.fetchall()
        for row in rows:
            activites.add(Activite(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return activites



def a_get_nums(nom):
    '''
    Récupère un set des `numero_equipements` en connaissant le `nom` exact d'une activité
    '''
    nums_equips = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT a.numero_equipements FROM activite a WHERE a.nom=?""", [nom])
        nums_equips = cur.fetchall()
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return nums_equips
