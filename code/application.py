# Python flask application to serve the webapp.

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging as logger
import os

application = Flask(__name__)
application.config['SECRET_KEY'] = 'supersecretkey123'

storeTitle = "The Medical Store"
offerDetails = [
    "10% discount on bulk orders",
    "50% off on 3 ply masks",
    "20% off on Face Shields",
    "Free Delivery Service",
    "10% off on Hand Sanitizers",
    "5% extra discount for members"
]

@application.route('/')
def index():
    return render_template('index.html', storeTitle=storeTitle, offers=offerDetails)

# products = [
#     {
#         "name": "3 Ply Mask",
#         "description": "(pack of 50)",
#         "price": "$14.99",
#         "img": "static/img/store/mask.jpg"
#     },
#     {
#         "name": "Hand Sanitizer",
#         "description": "(pack of 4)",
#         "price": "$3.99",
#         "img": "static/img/store/sanitizer.jpg"
#     },
#     {
#         "name": "3 Ply Mask",
#         "description": "(pack of 150)",
#         "price": "$19.99",
#         "img": "static/img/store/mask.jpg"
#     },
#     {
#         "name": "Hand Sanitizer",
#         "description": "(pack of 15)",
#         "price": "$14.99",
#         "img": "static/img/store/sanitizer.jpg"
#     }
# ]

# @application.route('/store')
# def store():
#     return render_template('store.html', storeTitle=storeTitle, products=products)


port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    logger.debug("Starting the Application")
    application.secret_key = os.urandom(12)
    application.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)