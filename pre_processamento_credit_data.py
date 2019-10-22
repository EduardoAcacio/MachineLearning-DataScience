# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:00:39 2019

@author: Eduardo Acacio

"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()
base.loc[base['age'] < 0]

base.drop('age', 1, inplace=True)

base.drop(base[base.age < 0].index, inplace=True)

base.mean()
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92
