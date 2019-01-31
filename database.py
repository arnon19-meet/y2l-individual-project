import datetime 
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)
def add_recipe(recipe_name,recipe_desc,recipe_ingredients,recipe_time):
    Drecipe = Recipe(recipe_name=recipe_name, recipe_desc=recipe_desc, recipe_ingredients=recipe_ingredients, recipe_time=recipe_time, )
    session.add(Drecipe)
    session.commit()

def get_recipes():
    Drecipe = session.query(Recipe).all()
    return Drecipe

def add_account(full_name, password, email, birthday):
    birthday = datetime.date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
    account=Account_info(password=password, birthday=birthday, full_name=full_name, email=email)
    session.add(account)
    session.commit()



def check_log_in(email, password):
    user = session.query(Account_info).filter_by(email=email).first()
    if user != None:
        if user.password!=password:
            return None
    return user

# def check_login_workplace(email, password):
#     return session.query(Workplace_info).filter_by(workplace_email=email, workplace_password=password)

def get_all_accounts():
    accounts = session.query(Account_info).all()
    return accounts

def get_recipe_by_name():
    reciname = session.query(Recipe).first()
    return reciname

def get_account_by_name():
    username= session.query.filter_by(full_name=full_name).first()
    return username