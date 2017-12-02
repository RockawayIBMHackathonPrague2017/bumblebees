#!/usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from math import *
from decimal import Decimal
from scipy.spatial import distance

def get_all_params(items):
    all_params = {}
    for item in items:
        params = item['PARAMS']
        for param in params:
            if all_params.get(param) == None:
                all_params[param] = []
            all_params[param].append(params[param])
    return all_params

def create_DataFrame(items):
    params = get_all_params(items)
    dataset = []
    ids = []
    for item in items:
        item_params = item['PARAMS']
        observation = []
        for prm in params:
            observation.append(item_params.get(prm))
        dataset.append(observation)
        ids.append(item['ITEM_ID'])

    dataset = np.array(dataset)
    return pd.DataFrame(dataset, columns=params), ids

class Distance():
    def __init__(self, items, drop=[]):
        self._items = items
        self.df, self.ids = create_DataFrame(items)
        self._drop_columns(drop)
        print('Distance obj: Creting DataFrame')
        self._remove_unsignificant_columns()
        print('Distance obj: Removing unsignificant columns')
        self._encode_color()
        print('Distance obj: Encoding special columns')
        self._fit()
        print('Distance obj: Fitting')

    def _drop_columns(self, columns):
        for item in columns:
            self.df = self.df.drop(item, 1)

    def _remove_unsignificant_columns(self):
        for col in self.df:
            v = self.df[col]
            percentage = sum(x == None for x in v) / len(v)
            if percentage > 0.9:
                self.df = self.df.drop(col, 1)

    def _encode_color(self):
        try:
            index = self.df.columns.get_loc('Barva')
            print(index)
            color_column = []
            for item in self.df.iloc[:, index]:
                if item == None:
                    color_column.append(0)
                else:
                    color_column.append(int('0x{}'.format(COLORS[item]), 16))
            self.df.iloc[:, index] = np.array(color_column)
        except KeyError:
            print('No color in DataFrame')

    def _fit(self):
        dummy_df = pd.get_dummies(self.df, drop_first=True)
        # add price
        product_price = [item['PRICE_VAT'] for item in self._items]
        dummy_df['PRICE_VAT'] = pd.Series(product_price, index=dummy_df.index)

        self.dummy_df = dummy_df
        X = self.dummy_df.iloc[:, :].values
        X = X.astype(np.float64)

        sc_X = MinMaxScaler(feature_range=(0, 1))
        # sc_X = StandardScaler()
        self.X = sc_X.fit_transform(X)

    def train_euclidean(self, observation):
        y = []
        for xi in self.X:
            y.append(np.sqrt(np.sum((self.X[observation, :] - xi) ** 2)))
        return y

    def train_cosine(self, observation):
        y = []
        for xi in self.X:
            y.append(distance.cosine(self.X[observation, :], xi))
        return y

    def train_manhattan(self, observation):
        y = []
        for xi in self.X:
            y.append(sum(abs(a - b) for a, b in zip(xi, self.X[observation, :])))
        return y

    def nth_root(self, value, n_root):
        root_value = 1 / float(n_root)
        return round(Decimal(value) ** Decimal(root_value), 3)

    def train_minkowski(self, observation, p_value):
        y = []
        for xi in self.X:
            y.append(self.nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(xi, self.X[observation, :])), p_value))
        return y

    def get_df(self, observation):
        df = pd.DataFrame(self.df)

        #df['Distance_eucl'] = pd.Series(self.train_euclidean(observation), index=df.index)
        df['Distance_cos'] = pd.Series(self.train_cosine(observation), index=df.index)
        #df['Distance_manh'] = pd.Series(self.train_manhattan(observation), index=df.index)
        #df['Distance_mink'] = pd.Series(self.train_minkowski(observation, 3), index=df.index)

        product_names = [item['PRODUCTNAME'] for item in self._items]
        product_desc = [item['DESCRIPTION'] for item in self._items]
        product_price = [item['PRICE_VAT'] for item in self._items]
        df['PRODUCTNAME'] = pd.Series(product_names, index=df.index)
        df['DESCRIPTION'] = pd.Series(product_desc, index=df.index)
        df['PRICE_VAT'] = pd.Series(product_price, index=df.index)
        return df
    def get_items(self, observation):
        print('get items', observation)
        items = self._items
        distances = self.train_cosine(observation)
        stacked = np.column_stack((distances, items))
        sorted = stacked[stacked[:,0].argsort()]
        return sorted[:,1]


COLORS = {
    'None': '0',
    'nerozlišuje se': '0',
    'vícebarevná': '0',

    'azurová': '00FFFF',
    'béžová': 'F5F5DC',
    'bílá': 'FFFFFF',
    'bílá/hnědá': 'FFFFFF',
    'bílá/růžová': 'FFFFFF',
    'bílá/stříbrná': 'FFFFFF',
    'bílá/zlatá': 'FFFFFF',
    'bílá/černá': 'FFFFFF',
    'bílá/červená': 'FFFFFF',
    'bílá/šedá': 'FFFFFF',
    'chrom': '808080',
    'cihlová': 'B22222',
    'dub': 'A52A2A',
    'fialová': 'EE82EE',
    'grafitově šedá': '808080',
    'hnědá': 'A52A2A',
    'hnědá/zelená': 'A52A2A',
    'khaki': 'F0E68C',
    'kávová/žula': 'A52A2A',
    'matná': '0000FF',
    'modrá': '0000FF',
    'modrá/oranžová': '0000FF',
    'modrá/tmavě modrá': '0000FF',
    'modrá/zelená': '0000FF',
    'modrá/černá': '0000FF',
    'měď': 'A52A2A',
    'námořní modrá': '0000FF',
    'oranžová': 'FFA500',
    'purpurová světlá': '9370DB',
    'růžová': 'FFC0CB',
    'růžová/fialová': 'FFC0CB',
    'stříbrná': 'C0C0C0',
    'stříbrná/modrá': 'C0C0C0',
    'stříbrná/růžová': 'C0C0C0',
    'stříbrná/černá': 'C0C0C0',
    'stříbrná/šedá': 'C0C0C0',
    'světle hnědá': 'A52A2A',
    'světle modrá': '0000FF',
    'světle růžová': 'FFC0CB',
    'světle zelená': '008000',
    'světle šedá': '808080',
    'titan': 'C0C0C0',
    'tmavě fialová': 'EE82EE',
    'tmavě modrá': '0000FF',
    'tmavě šedá': '808080',
    'tyrkysová': '0000FF',
    'vínová': 'FF0000',
    'zelená': '008000',
    'zlatá': 'FFD700',
    'zlatá/hnědá': 'FFD700',
    'černá': '000000',
    'černá/bílá': '000000',
    'černá/lesk': '000000',
    'černá/mat': '000000',
    'černá/modrá': '000000',
    'černá/oranžová': '000000',
    'černá/stříbrná': '000000',
    'černá/tmavě šedá': '000000',
    'černá/zelená': '000000',
    'černá/zlatá': '000000',
    'černá/červená': '000000',
    'černá/šedá': '000000',
    'černá/žlutá': '000000',
    'červená': 'FF0000',
    'červená/modrá': 'FF0000',
    'červená/černá': 'FF0000',
    'čirá': '808080',
    'šedá': '808080',
    'šedá/zelená': '808080',
    'šedá/černá': '808080',
    'žlutá': 'FFFF00',
    'žlutá/modrá': 'FFFF00',
    'žlutá/černá': 'FFFF00',
}

