from cloudant.query import Query
import json
import os
from cloudant import Cloudant

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


def execute_query(selector):
    findData = {
        "selector": selector,
        "fields": ["_id", "ITEM_ID", "PRODUCTNAME", "DESCRIPTION", "CATEGORYTEXT", "PRICE_VAT", "IMGURL", "URL",
                   "PARAMS"],
    }

    query = Query(db, selector=findData["selector"], fields=findData["fields"])
    resp = query(skip=0, r=1)
    return json.dumps(resp)


def get_all(limit):
    findData = {
        "fields": ["_id", "ITEM_ID", "PRODUCTNAME", "DESCRIPTION", "CATEGORYTEXT", "PRICE_VAT", "IMGURL", "URL",
                   "PARAMS"],
    }

    query = Query(db, selector={"_id": {"$gt": 0}}, fields=findData["fields"], limit=limit)
    resp = query(skip=0, r=1)
    return json.dumps(resp)