#!/usr/bin/env python3
"""contains our flask application object"""
import random

from flask import (Flask, render_template, url_for,
        request, redirect)
from werkzeug.utils import secure_filename

from storage.engine import storage_engine as storage
from models.product import Product
from models.product_image import ProductImage
from models.contact_detail import ContactDetail


app = Flask(__name__)

@app.route("/")
def home():
    products = [product for product in storage.get_all(Product)
                if product.should_be_featured()]
    random.shuffle(products)
    return render_template("home.html", products=products, gender=None)

@app.route("/products/")
def all_products():
    """return all products"""
    products = [product for product in storage.get_all(Product)]
    random.shuffle(products)
    return render_template('products.html', products=products)

@app.route("/products/men")
def mens_products():
    """return all men products"""
    mens_products = [product for product in storage.get_all(Product)
                     if product.is_male()]
    random.shuffle(mens_products)
    return render_template('products.html', products=mens_products, gender="m")

@app.route("/products/women")
def womens_products():
    """return all women products"""
    womens_products = [product for product in storage.get_all(Product)
                     if not product.is_male()]
    random.shuffle(womens_products)
    return render_template('products.html', products=womens_products,  gender="f")

@app.route("/product/<product_id>")
def product(product_id):
    """Returns a page for this product of this specific id"""
    product = storage.get(Product, product_id)
    if not product:
        redirect(url_for('home'))
    return render_template("product.html", product=product)

@app.post("/order")
def create_order():
    """Creates an order"""
    # expects: product_id customer_name phone
    pass

@app.route("/contact-us")
def contact_details():
    """Returns a page for this product of this specific id"""
    contact_details = [contact_detail
                       for contact_detail in storage.get_all(ContactDetail)
                       if not contact_detail.is_social_handle]
    social_handles = [contact_detail
                       for contact_detail in storage.get_all(ContactDetail)
                       if contact_detail.is_social_handle]
    return render_template("contact.html",
                           contact_details=contact_details,
                           social_handles=social_handles)


# admin
@app.route("/admin")
def admin():
    """Return admin homepage"""
    return render_template("admin/admin.html")

@app.route("/admin/products/")
def admin_products():
    """Return products page for admin"""
    products = storage.get_all(Product)

    return render_template("admin/products.html", products=products)

@app.route("/admin/product-creation-form")
def product_creation_form():
    """return product form page"""
    return render_template("admin/product_form.html",
                           action=url_for('create_product'))

@app.post("/admin/create-product")
def create_product():
    """Add product by admin and goes to a page to add images"""
    # get the form data from the request
    # if relevant form data isnt submitted ask user to submit again
    try:
        title = request.form["title"]
        description = request.form["description"]
        sex = request.form["sex"]
        price = request.form["price"]
        feature = False
        if request.form["feature"].upper() == "YES":
            feature = True

        product = Product(title=title,
                          description=description,
                          sex=sex,
                          price=price,
                          feature=feature)
        storage.add(product)
        storage.save()
        

        # after successful creation of product
        # redirect browser to product image adding page
        return redirect(url_for("admin_product", product_id=product.id))
    except KeyError: # report to user and ask user to submit form again
        return
    except:
        return redirect(url_for("admin_product", product_id=product.id))

@app.route("/admin/products/<product_id>/delete")
def admin_delete_product(product_id):
    """deletes product with such product_id"""
    storage.remove_by_id(Product, product_id)
    storage.save()
    return redirect(url_for("admin_products"))

@app.route("/admin/products/<product_id>")
def admin_product(product_id):
    """returns form that allows to upload an image for product"""
    product = storage.get(Product, product_id)
    images = product.images()
    number_of_images = len(images)
    return render_template("admin/product.html",
                           product=product,
                           images=images,
                           number_of_images=number_of_images)

@app.post("/admin/products/<product_id>/upload-image")
def upload_product_image(product_id):
    """handles product with product_id image upload"""
    try:
        uploaded_image_file = request.files["product_image"]
        if not uploaded_image_file.filename:
            # using KeyError is a tempral exception in this case
            raise KeyError("Filename doesnt exist so file wasnt uploaded:")
        # build save location
        base_save_location = ProductImage.IMAGES_BASE_LOCATION
        filename = secure_filename(uploaded_image_file.filename)
        save_location = base_save_location + filename
        # save uploaded image file
        uploaded_image_file.save(save_location)
        
        product_image = ProductImage(product_id=product_id,
                                     filename=filename)
        storage.add(product_image)
        storage.save()

        return redirect(url_for("admin_product",
                                product_id=product_id))

    except KeyError: # when file isnt uploaded ask for it again
        print("file upload failed")
        return "select an image file, go back and tr again"

@app.route("/admin/images/<image_id>/delete")
def admin_delete_image(image_id):
    """removes image"""
    # get the product the image is related to
    # so that you will return to the product's page
    product_id = storage.get(ProductImage, image_id).product_id
    storage.remove_by_id(ProductImage, image_id)
    storage.save()
    return redirect(url_for("admin_product", product_id=product_id))

@app.route("/admin/contact-detail-form")
def admin_contact_detail_form():
    contact_details = storage.get_all(ContactDetail)
    return render_template("admin/contact_detail_form.html",
                           contact_details=contact_details)

@app.post("/admin/create-contact-detail")
def admin_create_contact_detail():
    try:
        name = request.form["name"]
        value = request.form["value"]
        is_social_handle = False
        link = request.form.get("link")
        if request.form["is_social_handle"].upper() == "YES":
            is_social_handle = True

        contact_detail = ContactDetail(name=name,
                                       value=value,
                                       is_social_handle=is_social_handle,
                                       link=link)
        storage.add(contact_detail)
        storage.save()
    except:
        print("An error has occured while processing contact detail form")

    return redirect(url_for("admin_contact_detail_form"))

@app.route("/admin/contact-details/<contact_detail_id>/delete")
def admin_contact_detail_delete(contact_detail_id):
    storage.remove_by_id(ContactDetail, contact_detail_id)
    storage.save()
    return redirect(url_for("admin_contact_detail_form"))

@app.errorhandler(404)
def page_not_found(error):
    return "The Page You are looking for is ot found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    #pass
