from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.controllers.dojos import dojos
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# DISPLAY ROUTE--------
    # view ninja add page
@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)






# ACTION ROUTE--------
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save_ninja(data)
    #use dojo_id for url
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojos/{dojo_id}')

# how to get data
# how to redirect to /dojos/<int:id> with values