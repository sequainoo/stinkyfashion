"""a model of an image of a product"""
from base import Base


class ProductImage(Base):
    # class variables
    IMAGES_BASE_URL = "/static/images/"

    # instance variables
    product_id = ""
    filesystem_location = ""
    file_name = ""
    url = ""
    description = ""

    def __init__(self, **kwargs):
        #self.url = self.IMAGES_BASE_URL + self.file_name
        super().__init__(**kwargs)

    def url(self):
        """return the url of an image"""
        return self.IMAGES_BASE_URL + self.file_name

    def product(self):
        """returns the product for the image"""
        pass
