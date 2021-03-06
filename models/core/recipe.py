""" Contains the Recipe Model """

from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship
from models.core.user import User
from models.core.recipe_url import RecipeURL
from models.core.category import Category
from config import Config


class Recipe(Config.Base):
    """ Encapsulates a Recipe, it contains the user_id it belongs to """

    __tablename__ = 'recipe'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    description = Column(String(500))
    user_id = Column(BigInteger, ForeignKey(User.id))
    url_id = Column(BigInteger, ForeignKey(RecipeURL.id))
    category_id = Column(BigInteger, ForeignKey(Category.id))

    steps = relationship("RecipeStep", order_by="RecipeStep.num")
    quantity = relationship("Quantity")

    def __repr__(self):
        return '<Recipe: {}>'.format(self.name)

    @property
    def img_path(self):
        return "/static/img/%s.jpg" % str(self.url_id)
