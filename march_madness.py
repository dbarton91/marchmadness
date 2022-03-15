#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:35:03 2022

@author: bart924
"""

import pandas as pd # for reading csv's and creating the dataframe
import matplotlib.pyplot as plt #for plotting
import os #for changing the directory
import random
import numpy as np

#First Round Function

def finalfour(df):
    df2=pd.DataFrame() 
    startpos=0
    endpos=3
    firstcontender=df.iloc[startpos,2]
    secondcontender=df.iloc[endpos,2]
    firstcontenderfull=df.iloc[[startpos]]
    secondcontenderfull=df.iloc[[endpos]]
    
    dfa = roll(firstcontender,secondcontender,firstcontenderfull,secondcontenderfull,df2)
    
    startpos=1
    endpos=2
    firstcontender=df.iloc[startpos,2]
    secondcontender=df.iloc[endpos,2]
    firstcontenderfull=df.iloc[[startpos]]
    secondcontenderfull=df.iloc[[endpos]]
    
    dfb = roll(firstcontender,secondcontender,firstcontenderfull,secondcontenderfull,dfa)

    print (dfb)
    return dfb

def championship(df):
    df2=pd.DataFrame() 
    startpos=0
    endpos=1
    firstcontender=df.iloc[startpos,2]
    secondcontender=df.iloc[endpos,2]
    firstcontenderfull=df.iloc[[startpos]]
    secondcontenderfull=df.iloc[[endpos]]
    
    df2 = roll(firstcontender,secondcontender,firstcontenderfull,secondcontenderfull,df2)

    return df2

def matchup(df):
    dfmatchup=pd.DataFrame()
    no_of_teams=len(df.index)
    counter = int(no_of_teams/2)
    for n in range(counter):
        startpos = 0+n
        endpos = -1-n
        firstcontender=df.iloc[startpos,2]
        secondcontender=df.iloc[endpos,2]
        firstcontenderfull=df.iloc[[startpos]]
        secondcontenderfull=df.iloc[[endpos]]
        dfmatchup = roll(firstcontender,secondcontender,firstcontenderfull,secondcontenderfull,dfmatchup)
        
    return dfmatchup

def roll(firstcontender,secondcontender,firstcontenderfull,secondcontenderfull,df2):
    
    firstcontendermod=random.random()*secondcontender/(firstcontender+secondcontender)
    secondcontendermod=random.random()*firstcontender/(firstcontender+secondcontender)
    
    while firstcontendermod == secondcontendermod:
       firstcontendermod=random.random()*secondcontender/(firstcontender+secondcontender)
       secondcontendermod=random.random()*firstcontender/(firstcontender+secondcontender)
    
                    
    if firstcontendermod > secondcontendermod:
        df2 = df2.append(firstcontenderfull,ignore_index=True)
                # print('done')
        
    else:
        df2 = df2.append(secondcontenderfull,ignore_index=True) 
    
    return df2

def fight(df):
    df2=pd.DataFrame()
    teams=len(df.index)
       
    if teams == 2:
        dffinal = championship(df)
        return dffinal
    
    if teams%4 != 0:
        print ("Error: Number of teams will not work")
        return

    if teams == 4:
        dffinalfour = finalfour(df)
        return dffinalfour

    dfwest=df.loc[df["Side"] == "West"]
    dfwest=matchup(dfwest)
    dfsouth=df.loc[df["Side"] == "South"]
    dfsouth=matchup(dfsouth)
    dfeast=df.loc[df["Side"] == "East"]
    dfeast=matchup(dfeast)
    dfmidwest=df.loc[df["Side"] == "Midwest"]
    dfmidwest=matchup(dfmidwest)
    
    df2 = pd.concat([dfwest,dfsouth,dfeast,dfmidwest])
           
    return df2

currentdirectory="/Volumes/Dallin_postdoc/GitHub/"
csvfilename="March_Madness.csv"

os.chdir(currentdirectory)
df=pd.read_csv(csvfilename)

size = len(df.index)
n = 0
while size > 1:
    n = n+1
    stringn=str(n)
    df = fight(df)
    size = int(size/2)
    savename = currentdirectory+"Round"+stringn+".csv"
    print(savename, df)
    df.to_csv(savename)

champion = str(df.iloc[[0],[0]]) 
 
print("Congratulations ",champion,"!")



