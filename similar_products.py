#!/usr/bin/python
# -*- coding: utf8 -*-

import json
import db
from distance import Distance
import re

def get_items(category):
    items = db.execute_query({"CATEGORYTEXT": {"$regex": category}})
    return json.loads(items)['docs']

def get_similar_products(item):
    category = item['CATEGORYTEXT'].encode('utf-8')
    item_id = item['ITEM_ID']
    for item in categories:
        if item in category:
            index = categories[item].ids.index(item_id)
            items = list(categories[item].get_items(index))
            original_item = items.pop(0) # remove original item
            items, colors = get_color_products(items, original_item)
            items = items[0:10]
            items = add_labels(items, original_item)
            return {
                'docs': items,
                'colors': list(colors),
                'original': original_item
            }
    return {'docs': []}

def get_color_products(items, original_item):
    id = original_item['ITEM_ID'][:-3]
    color_items = []
    for item in items:
        #print(id, item['ITEM_ID'][:-3])
        if id == item['ITEM_ID'][:-3]:
            color_items.append(items.pop(0))
        else:
            return items, color_items

def add_labels(items, original_item):
    params = ['Interní paměť / ROM', 'Operační paměť / RAM', 'Kapacita baterie', 'Rozlišení fotoaparátu', 'Kapacita pevného disku', 'Paměť (RAM)']
    for item in items:
        item['LABELS'] = []
        if original_item['PRICE_VAT'] > item['PRICE_VAT']:
            item['LABELS'].append({'PARAM': 'PRICE_VAT', 'VALUE': item['PRICE_VAT']})
        for param in params:
            try:
                orig = int(re.findall("\d+", original_item['PARAMS'][param])[0])
                if orig < int(re.findall("\d+", item['PARAMS'][param])[0]):
                    item['LABELS'].append({'PARAM': param, 'VALUE': item['PARAMS'][param]})
            except Exception:
                pass
    return items

categories = {
    'Mobilní telefony a GPS': Distance(get_items('Mobilní telefony a GPS'), drop=['Výška','Hloubka','Distribuce']),
    'PC, kancelář': Distance(get_items('PC, kancelář'), drop=['Výška','Hloubka','Distribuce'])
}

