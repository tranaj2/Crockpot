""" Module provides functions for querying Ingredient Objects """

from models.core.ingredient import Ingredient
from operations import query_session

def by_name(name):
    """ Get an Ingredient by name """

    session = query_session.get_session()
    return session.query(Ingredient).filter(Ingredient.name == name).first()

def by_id(ingredient_obj):
    """ Get an Ingredient by ID """
    session = query_session.get_session()
    return session.query(Ingredient).filter(Ingredient.id == ingredient_obj).first()


def get_all():
    """ Get all ingredients """
    session = query_session.get_session()
    return session.query(Ingredient).all()
