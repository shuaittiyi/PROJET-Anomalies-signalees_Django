from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, 'type_anomalie_arrondissement/index.html')

#! /usr/bin/env python3
# coding: utf-

import sys
import pandas
import numpy
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

df=pandas.read_csv(r"C:\Users\shuai\Documents\FromationPython\anomalie-signalees\dans_ma_rue_ok.csv",sep = ';', encoding = 'unicode_escape', header = 0)
df = df.drop(['ADRESSE','DATE DECLARATION','geo_shape','ID DECLARATION',
         'CONSEIL DE QUARTIER','OUTIL SOURCE','INTERVENANT','ID_DMR','SOUS TYPE DECLARATION'], axis=1)
# Transformer tous les noms de colunnes en miniscule
df.columns = df.columns.str.lower()
# Remplacer les espaces de noms de colonnes par '_'
df.columns = df.columns.str.replace("[ ]", "_")

def f_data_frame(dataFrame) :
    # Ajouter les colonnes min et max de chaque ligne new_df
    dataFrame['min_idxmin'] = dataFrame.idxmin(axis=1)
    dataFrame['max_idxmax'] = dataFrame.idxmax(axis=1)
    # on cree des copie de colonnes min_idxmin et max_idxmax  que l'on nomme min et max
    dataFrame['min'] = dataFrame['min_idxmin'].tolist()
    dataFrame['max'] = dataFrame['max_idxmax'].tolist()
    # Suppression de colonnes min_idxmax et max_idx
    # car elles nous servent à rien (on les a copié)
    dataFrame = dataFrame.drop(['min_idxmin', 'max_idxmax'],axis=1)
    # la dataframe finale
    return dataFrame.reset_index()
    
df_3 = f_data_frame(pandas.crosstab([df['type_declaration']], df['arrondissement']))

print(df_3)
    
colonnes_arrondissement = df_3.columns[1:len(df_3.columns)-2]    
for i in range(len(colonnes_arrondissement)) :
    if i < 10 :
        df_iloc = df_3.iloc[i:i+1]
        sns.set_style("ticks")
        sns.set_theme()
        sns.color_palette('Reds',20)
        df_iloc.plot(
            x        = "type_declaration",
            y        = colonnes_arrondissement,
            kind     = "bar",
            subplots = False,
           title    = "Anomalies signalées",
           xlabel   = df_iloc['type_declaration'][i],
            ylabel   = "Nombre d'anomalies signalées",
            rot      = 0,
            xticks   = [],
        #    colormap = 'rainbow',
           colormap = "RdBu",
            grid = True)

