import flask
from flask import redirect, render_template, request, url_for

app = flask.Flask(__name__)
print(__name__)
print(flask.__name__)

data = {
    "1": "Fraise",
    "200": "Tomates",
    "3": "Un autre titre"
}

# @app.route('/hello')
# def hello_world():
#     return "Hello World"

# @app.route('/hello/<name>')
# def hello_world(name):
#     print(type(name))
#     return "Hello %s" % name

# pour récupérer un int
@app.route('/hello/<int:id>')
def hello_world(id):
    # print(type(id))
    print(data.keys())
    if str(id) in data.keys():
        return "Hello %s" % data[str(id)]
    else:
        return "Erreur"  
    # return "Hello %d" % id

# # pour récupérer un float
# @app.route('/hello/<float:id>')
# def hello_world(id):
#     print(type(id))
#     return "Hello %f" % id

@app.route('/hello/<nom>')
def hello_guest(nom):
    return render_template('hello_guest.html', name=nom, categories=["Fruits", "Légumes"])

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for('hello_world', id=1))
    else:
        return redirect(url_for('hello_guest', name="Guest"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form.get('prenom') # ou request.form['prenom']
        print(data)
        return "Votre prénom est {}".format(data)
    return render_template('login.html')

# Récupérer le texte depuis le champ du texte et l'afficher dans la même page HTML
# @app.route('/login', methods=["POST"])
# def data():
    


#if __name__ == "__main__":
app.run(debug=True)