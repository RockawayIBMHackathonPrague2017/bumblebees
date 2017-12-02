#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask
import atexit
import cf_deployment_tracker
import os
import json
import similar_products
import db

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def home():
    return "Nothing to see here"


@app.route('/all', methods=['GET'])
def get_20_results():
    return db.get_all(20)


@app.route('/filtered/<string:_id>', methods=['GET'])
def filtered_by_id(_id):
    product = json.loads(db.execute_query({"_id": _id}))['docs']
    if len(product) == 1:
        return json.dumps({
            'docs': list(similar_products.get_similar_products(product[0]))[0:10]
        }) #db.execute_query({"CATEGORYTEXT": product['docs'][0]["CATEGORYTEXT"]})
    else:
        return json.dumps({"docs": []})


@app.route('/filtered/category/<string:category>', methods=['GET'])
def filtered_by_category(category):
    return db.execute_query({"CATEGORYTEXT": {"$regex": category}})


@app.route('/filtered/selector/<string:selector>', methods=['GET'])
def filtered_by_selector(selector):
    # https://console.bluemix.net/docs/services/Cloudant/api/cloudant_query.html#query
    return db.execute_query(json.loads(selector))


@atexit.register
def shutdown():
    if db.client:
        db.client.disconnect()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
