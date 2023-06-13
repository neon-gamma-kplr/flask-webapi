import psycopg2
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# récupérer toutes les données de la base de données et les retourner sous forme de réponse JSON
@app.route('/afficher', methods=['GET'])
def get_all():
    # Connection à la base de données
    try:
        connexion = psycopg2.connect(dbname='nxsoxgro',
                                    user='nxsoxgro',
                                    password='vpvuRLZZoKafSSjF9mfm0z5Ehj0x1Hcg',
                                    host='horton.db.elephantsql.com')
        print("Database connected successfully")
    except:
        print("Database not connected successfully")
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM data")
    lignes = curseur.fetchall()
    connexion.commit()
    curseur.close()
    connexion.close()
    return jsonify(lignes)

# récupérer un seul élément de données par son ID et le retourner sous forme de réponse JSON
@app.route('/afficher/<int:id>', methods=['GET'])
def get_one(id):
    # Connection à la base de données
    try:
        connexion = psycopg2.connect(dbname='nxsoxgro',
                                    user='nxsoxgro',
                                    password='vpvuRLZZoKafSSjF9mfm0z5Ehj0x1Hcg',
                                    host='horton.db.elephantsql.com')
        print("Database connected successfully")
    except:
        print("Database not connected successfully")
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM data WHERE id = %s", str(id))
    ligne = curseur.fetchone()
    connexion.commit()
    curseur.close()
    connexion.close()
    return jsonify(ligne)

# # ajouter un nouvel élément de données à la base de données et retourner une réponse JSON indiquant le succès ou l'échec
# @app.route('/ajouter', methods=['POST'])
# def add_one(element):
#     resultat = []
#     curseur.execute("INSERT INTO data (name, value) VALUES (%s, %s)", (element, element))
#     lignes = curseur.fetchall()
#     for ligne in lignes:
#         resultat.append(ligne)
#     return jsonify(resultat)
    
# # mettre à jour un élément de données existant dans la base de données et retourner une réponse JSON indiquant le succès ou l'échec
# @app.route('/modifier/<int:id>', methods=['PUT'])
# def update(id):
#     nom = request.args.get("name")
#     valeur = request.args.get("value")
#     resultat = []
#     curseur.execute("UPDATE SET data")
#     lignes = curseur.fetchall()
#     for ligne in lignes:
#         resultat.append(ligne)
#     return jsonify(resultat)

# # mettre à jour un élément de données existant dans la base de données et retourner une réponse JSON indiquant le succès ou l'échec
# @app.route('/supprimer/<int:id>', methods=['DELETE'])
# def delete(id):
#     resultat = []
#     curseur.execute("DELETE FROM data WHERE id = %s", id)
#     lignes = curseur.fetchall()
#     for ligne in lignes:
#         resultat.append(ligne)
#     return jsonify(resultat)

app.run()