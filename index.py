from cloudant import Cloudant
from cloudant.query import Query
from flask import Flask, render_template, request, jsonify
import atexit
import cf_deployment_tracker
import os
import json

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

db_name = 'products'
client = None
db = None
project_dir = os.path.dirname(os.path.realpath(__file__))

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile(os.path.join(project_dir, 'vcap-local.json')):
    with open(os.path.join(project_dir, 'vcap-local.json')) as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)


def find_relevant(selector):
    findData = {
        "selector": selector,
        "fields": ["_id", "ITEM_ID" "PRODUCTNAME", "DESCRIPTION", "CATEGORYTEXT", "PRICE_VAT", "IMGURL", "URL",
                   "PARAMS"],
    }

    query = Query(db, selector=findData["selector"], fields=findData["fields"])
    resp = query(skip=0, r=1)
    return resp["docs"]


def get_all(limit):
    findData = {
        "fields": ["_id", "ITEM_ID" "PRODUCTNAME", "DESCRIPTION", "CATEGORYTEXT", "PRICE_VAT", "IMGURL", "URL",
                   "PARAMS"],
    }

    query = Query(db, selector=findData["selector"], fields=findData["fields"])
    resp = query(skip=0, limit=limit, r=1)
    return resp["docs"]


# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def home():
    # return render_template(os.path.join(project_dir, 'static\index.html'))
    return render_template('index.html')


@app.route('/all', methods=['GET'])
def get_20_results():
    return get_all(20)


@app.route('/filtered/<int:product_id>', methods=['GET'])
def filtered_by_id(product_id):
    product = find_relevant({"ITEM_ID": product_id})
    if product.length == 1:
        return find_relevant({"CATEGORYTEXT": product[0]["CATEGORYTEXT"]})
    else:
        return []


@app.route('/filtered/category/<string:category>', methods=['GET'])
def filtered_by_category(category):
    return find_relevant({"&CATEGORYTEXT": category})


@app.route('/filtered/selector/<string:selector>', methods=['GET'])
def filtered_by_category(selector):
    return find_relevant(json.loads(selector))


@atexit.register
def shutdown():
    if client:
        client.disconnect()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
