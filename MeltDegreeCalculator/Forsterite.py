# -*- coding: utf-8 -*-
"""
@author: jiale
"""

import numpy as np
import pandas as pd

def funcFo_Mg(df):
    
    dfapp = df.copy()
    dfapp['Mg_num'] = dfapp['MgOo (wt%)'] / 40.3044 / (dfapp['MgOo (wt%)'] / 40.3044 + dfapp['FeOo (wt%)'] / 71.844)
    
    popt = [2.395e-2, 3.469e-4, 2.084]
    dfapp['Foo'] = np.where(dfapp['Mg_num'] > 0.92, dfapp['Mg_num'], 
                            popt[0] * dfapp['Mg_num']**2 + popt[1] * dfapp['Mg_num'] + popt[2])
    df['Foo']=dfapp['Foo']

    return df


def F_Fo(df):
    dfapp = df.copy()
    
    dfapp['Fo'] = pd.to_numeric(dfapp['Fo'], errors='coerce')
    dfapp['Foo'] = pd.to_numeric(dfapp['Foo'], errors='coerce')
    
    dfapp['F-Fosterite'] = 14.43*(dfapp['Fo']-dfapp['Foo'])

    return dfapp
