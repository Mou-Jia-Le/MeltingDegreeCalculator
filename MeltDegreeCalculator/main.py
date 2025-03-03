# -*- coding: utf-8 -*-
"""
@author: jiale
"""

print('\n>> loading ... \n')


import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

import pandas as pd
import tools
import Forsterite
import MassBalance


data_input = pd.read_excel('data_input.xlsx')

# default parameter for calculation
#Foo       = 0.897
#MgOo      = 37.8
#FeOo        = 8.02
data = data_input.copy()



if tools.question("\n Calculate melting degrees using olivine Fosterite? "):
    if tools.question("\n Use default initial Fo?\n"):
        data['Foo'] = 0.897
    elif tools.question("\n Use initial whole rock Mg# to estimate initial Fo?"):
        data = Forsterite.funcFo_Mg(data)
    data = Forsterite.F_Fo(data)


if tools.question("\n Calculate melting degrees using whole rock composition? "):
    if tools.question("\n Use default initial whole rock composition?\n"):
        data['MgOo (wt%)'] = 37.8
        data['FeOo (wt%)'] = 8.05
    data = MassBalance.MassBalance(data)

data.to_csv('output_MeltingDegrees.csv', index=False)

print('\n >> Results saved to csv!\n')
