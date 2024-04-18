"""a model of an image of a product"""
import os

from .base import Base


class ProductImage(Base):
    # class variables
    IMAGES_BASE_URL = "/static/images/"
    IMAGES_BASE_LOCATION = "web_app/static/images/"

    # instance variables
    product_id = ""
    #filesystem_location = ""
    filename = ""
    url = ""
    #description = ""

    def __init__(self, **kwargs):
        #self.url = self.IMAGES_BASE_URL + self.file_name
        super().__init__(**kwargs)

    def url(self):
        """return the url of an image"""
        return self.IMAGES_BASE_URL + self.filename

    def product(self):
        """returns the product for the image"""
        pass

    def delete(self):
       """delete the image file from the file system"""
       # image_file location on file system
       file_location = self.IMAGES_BASE_LOCATION + self.filename
       # check if path exists
       if os.path.exists(file_location):
           os.remove(file_location)
       # if it does delete the file
       # then clean object from mem
       del self