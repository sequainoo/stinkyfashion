#!/usr/bin/env python3
from storage.engine import storage_engine as storage
from models.product import Product
from models.product_image import ProductImage


product1 = storage.get_all(Product)[0]
product2 = storage.get_all(Product)[1]
storage.remove(product1)

products = storage.get_all(Product)
product_images = storage.get_all(ProductImage)

if len(products) == 1 and product1 not in products:
    print('product 1 is removed from storage')
else:
    print('product 1 was not removed from storage')

if len(product_images) == 1:
    if product2.images()[0] in product_images:
        print("product 1 related images removed from storage")
    else:
        print("remove operation did remove non related object from store")
else:
    print("related objects/images could not be removed from storage")

for product in products:
    print(product)
print()
for image in product_images:
    print(image)

#product1_related_objects = product1.related_objects()

#for product1_related_object in product1_related_objects:
#    print(str(product1_related_object))

#product1_images = product1.images()

#for product1_image in product1_images:
#    print(str(product1_image))

#all_product_images = storage.get_all(ProductImage)

#for product_image in all_product_images:
#    product_image.product_id = product1.id

#storage.save()
#for product_image in all_product_images:
#    print(str(product_image))
#print(product1.id)

# creates two products and related images and adds to storage
"""product1 = Product(name="Kaftan", description="brown and cream")
product1_image1 = ProductImage(product_id=product1.id, description="product1 image1")
product1_image2 = ProductImage(product_id=product1.id, description="product1 image2")
#product1image1.product_id = product1.id

product2 = Product(name="handbag", description="yellow and white handbag")
product2_image1 = ProductImage(product_id=product2.id, description="product2 image1")

storage.add(product1, product2, product1_image1, product1_image2, product2_image1)"""
#storage.save()
#storage.add(product1)
#print(image1)


#if not image1:
#    print('correct')
