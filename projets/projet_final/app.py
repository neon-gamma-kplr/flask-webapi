import flask
from flask_login import login_required, current_user, login_user, logout_user
from flask import redirect, render_template, request, url_for
from application.models import engine, Session


app = flask.Flask(__name__)


@app.route('/')
@login_required
def index():
    Session.
    with engine.connect() as connection:
        result_set = connection.execute(text('SELECT * FROM api_sold ORDER BY date DESC'))
    return render_template('index.html', tableau = result_set.fetchall())


def delete(entry_id):
    
    with engine.connect().execution_options(autocommit=True) as connection:
        result_set = connection.execute(text("DELETE FROM api_sold WHERE id = %s", str(entry_id)))
    if result_set.fetchone() == :
        print("La dépense a été supprimée avec succès !")
        return redirect(url_for('index'))
    else:
        print("Erreur. La suppression a échoué.")


@app.route('/hello/<nom>')
def hello_guest(nom):
    return render_template('profile.html', name=current_user)


@app.route('/hello/<nom>')
def hello_guest(nom):
    return render_template('login.html', name=nom, categories=["Fruits", "Légumes"])


@app.route('/login', methods=['POST'])
def login_post():
    data = request.form
    data['email'], data['password'], et data['remember']
    ("SELECT * FROM User WHERE email = %s", data['email'])
    if and data['password'] == :
    login_user()
    return render_template('login.html', name=nom)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello_guest', name="Guest"))


@app.route('/dashboard')
@login_required
def dashboard():
    SESSION.rollback()
    income_vs_expense = func.sum() SELECT FROM WHERE
    category_comparison = func.sum()
    dates = func.sum()
    income_category = []
    labels = []
    over_time_expenditure = []
    income_vs_expense = {}
    income_category = {}
    income_category_labels = {}
    over_time_expenditure = {}
    dates_labels = {}
    return render_template('dashboard.html', name=current_user)


if __name__ == "__main__":
    app.run(debug=True)