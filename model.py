from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Account_info(Base):
    __tablename__="account_info"
    user_number=Column(Integer,primary_key=True)
    user_name=Column(String)
    password=Column(Integer)
    confirm_password=Column(Integer)
    full_name=Column(String)
    birthday=Column(Date)
    gender=Column(Boolean)
    email=Column(String)

class Recipe(Base):
    __tablename__ = "Drecipe"
    id = Column(Integer, primary_key = True)
    recipe_name = Column(String)
    recipe_desc = Column(String)
    recipe_ingredients = Column(String)
    recipe_time = Column(Integer)
    