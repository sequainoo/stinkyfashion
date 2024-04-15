#!/usr/bin/env python
"""Model of product being sold hwihc is a cloth"""
from .base import Base


class Product(Base):
    name = ""
    description = ""
    price = 0.0
    #images_ids = [] # a list of ids of image objects

    def __init__(self, **kwargs):
        #self._images = kwargs['images_ids']
        #del kwargs['images_ids']
        super().__init__(**kwargs)

    def images(self):
        """returns a list of ProductImage objects related to this object"""
        from storage.engine import storage_engine
        from .product_image import ProductImage
        return [image 
                for image in storage_engine.get_all(ProductImage)
                if image.product_id == self.id]

    #def __delete__(self):
    #    """it finds associated objects (by_id) and execute delete on them"""
    #    pass

    def related_objects(self):
        return self.images()
