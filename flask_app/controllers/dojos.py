from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

# DISPLAY ROUTES ---------
    #home page will go to /dojos page
@app.route('/')
def index():
    return redirect('/dojos')
    
    #make as home page
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', dojos= dojos)

    #show dojos
@app.route('/dojos/<int:id>')
def show_dojo(id):
    data ={
        "id": id
    }
    ninjas = Dojo.get_one(data)
    print(ninjas)
    return render_template('show_dojo.html', ninjas = ninjas)


# ACTION ROUTES-------
    #creating a new dojo
@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')
    
