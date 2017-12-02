#!/usr/bin/python
# -*- coding: utf8 -*-

import json
import db
from distance import Distance

def get_items(category):
    items = db.execute_query({"CATEGORYTEXT": {"$regex": category}})
    return json.loads(items)['docs']

def get_similar_products(item):
    category = item['CATEGORYTEXT'].encode('utf-8')
    item_id = item['ITEM_ID']
    for item in categories:
        if item in category:
            index = categories[item].ids.index(item_id)
            return categories[item].get_items(index)

categories = {
    'Mobilní telefony a GPS': Distance(get_items('Mobilní telefony a GPS'), drop=['Výška','Hloubka','Distribuce']),
    'PC, kancelář': Distance(get_items('PC, kancelář'), drop=['Výška','Hloubka','Distribuce'])
}

