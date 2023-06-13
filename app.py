import flask
from flask import redirect, url_for

app = flask.Flask(__name__)

print(__name__)
print(flask.__name__)

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
    print(type(id))
    return "Hello %d" % id

# # pour récupérer un float
# @app.route('/hello/<float:id>')
# def hello_world(id):
#     print(type(id))
#     return "Hello %f" % id

@app.route('/hello/<name>')
def hello_guest(name):
    return "Hello %s" % name

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for('hello_world', id=1))
    else:
        return redirect(url_for('hello_guest', name="Guest"))

#if __name__ == "__main__":
app.run(debug=True)