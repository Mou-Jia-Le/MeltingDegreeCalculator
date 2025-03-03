# -*- coding: utf-8 -*-
"""
@author: jiale
"""

from scipy.optimize import fsolve

def MassBalance(df):
    dfapp = df.copy()  
    FeOrl = dfapp['FeO (wt%)']
    MgOrl = dfapp['MgO (wt%)']
    MgOol = dfapp['MgOo (wt%)']
    FeOol = dfapp['FeOo (wt%)']

    def func1(MgOm, FeOr, MgOr, FeOo, MgOo):
        a = FeOr*(MgOr-MgOo)-MgOr*(FeOr-FeOo)
        eq = MgOm*((FeOo-FeOr)+(MgOr-MgOo)*FeOr/MgOr/(0.381-0.774/MgOm+0.998/(MgOm**2)))-a
        return eq

    Farray = []
    MgOmarray = []

    for FeOr, MgOr, FeOo, MgOo in zip(FeOrl, MgOrl, FeOol, MgOol):
        MgOm = fsolve(func1, [37.8], args=(FeOr, MgOr, FeOo, MgOo))[0]  # Extract scalar
        F = (MgOo-MgOr)/(MgOm-MgOr)
        Farray.append(F)
        MgOmarray.append(MgOm)

    dfapp['F-Whole Rock'] = Farray
    dfapp['MgOm (wt%)'] = MgOmarray
    dfapp['FeOm (wt%)'] = (dfapp['FeOo (wt%)']-dfapp['FeO (wt%)']*(1-dfapp['F-Whole Rock']))/dfapp['F-Whole Rock']
    dfapp['DMgO'] = dfapp['MgO (wt%)']/dfapp['MgOm (wt%)']
    dfapp['DFeO'] = dfapp['FeO (wt%)']/dfapp['FeOm (wt%)']
    dfapp['KDFe/Mg'] = dfapp['DFeO']/dfapp['DMgO']

    return dfapp
