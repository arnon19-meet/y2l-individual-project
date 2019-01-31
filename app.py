from flask import Flask, render_template, url_for, redirect, request, session


from database import add_recipe, get_recipes, add_account, check_log_in, get_all_accounts, get_recipe_by_name

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('home.html',accounts= get_all_accounts())



@app.route('/register_account', methods=['GET', 'POST'])
def register_account():
    if request.method == 'GET':
        return render_template('register_account.html')
    else:
        full_name = request.form["fullname"]
        password = request.form["password"]
        check_password = request.form["check_pwd"]
        email = request.form["Email"]
        birthday = request.form["birthday"].split("/")
        add_account(name, password, email, birthday)
        session["loggedin"] = True
        session["account"] = True
        session["email"] = email
        
        return redirect(url_for("recipepage"))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form["Email"]
        password=request.form["password"]
        checking=check_log_in(email,password)
        if checking == None:
            return render_template('login.html', error = "retry password")
        else:
            session["loggedin"] = True
            session["account"] = True
            session["email"] = _email
            return redirect(url_for('recipepage'))
    return render_template('home.html')

@app.route('/recipepage')
def recipepage():
    # if session.get("loggedin") == True:
    return render_template('recipepage.html', Drecipe=get_recipes())
    # else:
    #     return redirect(url_for("login"))


@app.route('/add_recipe', methods=['GET','POST'])
def add_recipe_route():
    if request.method == 'GET':
        return render_template('add_recipe.html')
    else:
        recipe_name = request.form["name"]
        recipe_desc = request.form["desc"]
        recipe_ingredients = request.form["ingredients"]
        recipe_time = request.form["time"]
        add_recipe(recipe_name,recipe_desc,recipe_ingredients,recipe_time)
        return redirect(url_for("recipepage"))

@app.route('/srecipe/<string:recipename>')
def srecipe(recipename):
    # if session.get("loggedin") == True:
    recipename=get_recipe_by_name()
    Drecipe=get_recipe_by_name()
    return render_template('srecipe.html', Drecipe=get_recipes())

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect(url_for("home"))

@app.route('/profile')
def profiles():
    if session.get("loggedin") == True:
        return render_template('profile.html', accounts= get_all_accounts(), ) 
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
