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
            items = categories[item].get_items(index)
            items, colors = get_color_products(items)
            return {
                'docs': list(items)[0:10],
                'colors': list(colors)
            }
    return {'docs': []}

def get_color_products(items):
    id = items.pop(0)['ITEM_ID'][:-3]
    color_items = []
    for item in items:
        print(id, item['ITEM_ID'][:-3])
        if id == item['ITEM_ID'][:-3]:
            color_items.append(id.pop(0))
        else:
            return items, color_items


categories = {
    'Mobilní telefony a GPS': Distance(get_items('Mobilní telefony a GPS'), drop=['Výška','Hloubka','Distribuce']),
    'PC, kancelář': Distance(get_items('PC, kancelář'), drop=['Výška','Hloubka','Distribuce'])
}

