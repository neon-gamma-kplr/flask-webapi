import psycopg2
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

elements = [
    {
        "id": 1,
        "nom": "Jean",
        "valeur": 5
    },
    {
        "id": 2,
        "nom": "Pierre",
        "valeur": 83
    },
    {
        "id": 3,
        "nom": "Sarah",
        "valeur": 54
    },
    {
        "id": 4,
        "nom": "Pascal",
        "valeur": 23
    },
    {
        "id": 5,
        "nom": "Julie",
        "valeur": 2
    },
    {
        "id": 6,
        "nom": "Olivier",
        "valeur": 47
    },
    {
        "id": 7,
        "nom": "Denise",
        "valeur": 126
    }
]


def connect():
    try:
        connexion = psycopg2.connect(dbname='nxsoxgro',
                                     user='nxsoxgro',
                                     password='vpvuRLZZoKafSSjF9mfm0z5Ehj0x1Hcg',
                                     host='horton.db.elephantsql.com')
        print("Database connected successfully")
    except:
        print("Database not connected successfully")
    return connexion


# récupérer toutes les données de la base de données et les retourner sous forme de réponse JSON
@app.route('/afficher')
def get_all():
    connexion = connect()
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM data")
    lignes = curseur.fetchall()
    curseur.close()
    connexion.close()
    return jsonify(lignes)


# récupérer un seul élément de données par son ID et le retourner sous forme de réponse JSON
@app.route('/afficher/<int:id>')
def get_one(id):
    connexion = connect()
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM data WHERE id = %s", str(id))
    ligne = curseur.fetchone()
    curseur.close()
    connexion.close()
    return jsonify(ligne)


# ajouter un nouvel élément de données à la base de données et retourner une réponse JSON indiquant le succès ou l'échec
@app.route('/ajouter/<int:id>', methods=['GET', 'POST'])
def add_one(id):
    connexion = connect()
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO data (name, value) VALUES (%s, %s)",
                    (elements[id - 1]["nom"], elements[id - 1]["valeur"]))
    connexion.commit()
    message = f"{curseur.rowcount} record inserted."
    curseur.close()
    connexion.close()
    return message


# mettre à jour un élément de données existant dans la base de données et retourner une réponse JSON indiquant le succès ou l'échec
@app.route('/modifier/<nom>/<valeur>', methods=['GET', 'PUT'])
def update(nom, valeur):
    connexion = connect()
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("UPDATE data SET value = %s WHERE name = %s", (valeur, nom))
    message = f"{curseur.rowcount} record modified."
    connexion.commit()
    curseur.close()
    connexion.close()
    return message


# mettre à jour un élément de données existant dans la base de données et retourner une réponse JSON indiquant le succès ou l'échec
@app.route('/supprimer/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    connexion = connect()
    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM data WHERE id = %s", str(id))
    message = f"{curseur.rowcount} record deleted."
    connexion.commit()
    curseur.close()
    connexion.close()
    return message


app.run(debug=True)