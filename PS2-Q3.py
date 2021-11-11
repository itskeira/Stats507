# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Problem Set 2 - Question 3 

# *Stats 507, Fall 2021*
#
# Han Qiu  
# September 30, 2021

import numpy as np
from timeit import default_timer as timer
from statistics import mean
from itertools import groupby
from collections import defaultdict
import pandas as pd
import re

# 3.a

# +
url1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT'
url2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT'
url3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT'
url4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'

cols = ['SEQN', 'RIDAGEYR', 'RIDRETH3','DMDEDUC2','DMDMARTL',
        'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']

df1 = pd.read_sas(url1)
new_df1 = df1[cols].copy()
new_df1['cohort']='1'
final_df1 = new_df1.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'interview/examination status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight', 
                            'cohort'], axis=1, inplace=False)

df2 = pd.read_sas(url2)
new_df2 = df2[cols].copy()
new_df2['cohort']='2'
final_df2 = new_df2.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'interview/examination status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight', 
                            'cohort'], axis=1, inplace=False)

df3 = pd.read_sas(url3)
new_df3 = df3[cols].copy()
new_df3['cohort']='3'
final_df3 = new_df3.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'interview/examination status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight', 
                            'cohort'], axis=1, inplace=False)

df4 = pd.read_sas(url4)
new_df4 = df4[cols].copy()
new_df4['cohort']='4'
final_df4 = new_df4.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'interview/examination status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight', 
                            'cohort'], axis=1, inplace=False)


convert_dict = {'id': int,
                'age': int,
                'race/ethnicity': 'category',
                'education': 'category',
                'marital status': 'category',
                'interview/examination status': 'category',
                'masked variance pseudo-psu': int,
                'masked variance pseudo-stratum': int,
                '2 year mec exam weight': float,
                '2 year interview weight':float,
                'cohort': int
               }

demo_df = [final_df1, final_df2, final_df3, final_df4]
final_demo_df = pd.concat(demo_df,axis=0)
final_demo_df = final_demo_df.astype(convert_dict)

# save to pickle format
final_demo_df.to_pickle("./demo.pkl")
#df = pd.read_pickle("./demo.pkl")

# check column types
print(final_demo_df.dtypes)

final_demo_df.head()
# -

# 3.b

# +
url_d1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT'
url_d2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT'
url_d3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT'
url_d4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT'

# cohort 1

dd1 = pd.read_sas(url_d1)
dental_col1 = ['SEQN', 'OHDDESTS']

for col in dd1.columns:
    if re.match(r'OHX\d+\dTC',col) or re.match(r'OHX\d+\d+CTC',col):
        dental_col1.append(col)

dental_df1 = dd1[dental_col1].copy()
dental_df1['cohort']='1'


dental_col1[0] = 'id'
dental_col1[1] = 'dentition status code'
for i in range(len(dental_col1)):
    if re.match('^OHX.*CTC$',dental_col1[i]):
        dental_col1[i] = 'coronal tooth count '+ dental_col1[i][3:5]
    elif re.match('^OHX.*TC$',dental_col1[i]):
        dental_col1[i] = 'tooth count '+ dental_col1[i][3:5]
            
dental_col1.append('cohort')
den1 = dental_df1.set_axis(dental_col1, axis=1, inplace=False)

# cohort 2

dd2 = pd.read_sas(url_d2)
dental_col2 = ['SEQN', 'OHDDESTS']

for col in dd2.columns:
    if re.match(r'OHX\d+\dTC',col) or re.match(r'OHX\d+\d+CTC',col):
        dental_col2.append(col)

dental_df2 = dd2[dental_col2].copy()
dental_df2['cohort']='2'

dental_col2[0] = 'id'
dental_col2[1] = 'dentition status code'
for i in range(len(dental_col2)):
    if re.match('^OHX.*CTC$',dental_col2[i]):
        dental_col2[i] = 'coronal tooth count '+ dental_col2[i][3:5]
    elif re.match('^OHX.*TC$',dental_col2[i]):
        dental_col2[i] = 'tooth count '+ dental_col2[i][3:5]
            
dental_col2.append('cohort')
den2 = dental_df2.set_axis(dental_col2, axis=1, inplace=False)

# cohort 3

dd3 = pd.read_sas(url_d3)
dental_col3 = ['SEQN', 'OHDDESTS']

for col in dd3.columns:
    if re.match(r'OHX\d+\dTC',col) or re.match(r'OHX\d+\d+CTC',col):
        dental_col3.append(col)

dental_df3 = dd3[dental_col3].copy()
dental_df3['cohort']='3'

dental_col3[0] = 'id'
dental_col3[1] = 'dentition status code'
for i in range(len(dental_col3)):
    if re.match('^OHX.*CTC$',dental_col3[i]):
        dental_col3[i] = 'coronal tooth count '+ dental_col3[i][3:5]
    elif re.match('^OHX.*TC$',dental_col3[i]):
        dental_col3[i] = 'tooth count '+ dental_col3[i][3:5]
            
dental_col3.append('cohort')
den3 = dental_df3.set_axis(dental_col3, axis=1, inplace=False)

# cohort 4

dd4 = pd.read_sas(url_d4)
dental_col4 = ['SEQN', 'OHDDESTS']

for col in dd4.columns:
    if re.match(r'OHX\d+\dTC',col) or re.match(r'OHX\d+\d+CTC',col):
        dental_col4.append(col)

dental_df4 = dd4[dental_col4].copy()
dental_df4['cohort']='4'

dental_col4[0] = 'id'
dental_col4[1] = 'dentition status code'
for i in range(len(dental_col4)):
    if re.match('^OHX.*CTC$',dental_col4[i]):
        dental_col4[i] = 'coronal tooth count '+ dental_col4[i][3:5]
    elif re.match('^OHX.*TC$',dental_col4[i]):
        dental_col4[i] = 'tooth count '+ dental_col4[i][3:5]
            
dental_col4.append('cohort')
den4 = dental_df4.set_axis(dental_col4, axis=1, inplace=False)

# combine
dental_df = [den1, den2, den3, den4]
final_dental = pd.concat(dental_df,axis=0)
final_dental[dental_col1] = final_dental[dental_col1].astype('category')
final_dental[['id','cohort']] = final_dental[['id','cohort']].astype(int)

# check column types
print(final_dental.dtypes)

# save to pickle format
final_dental.to_pickle("./dental.pkl")
#df = pd.read_pickle("./dental.pkl")

final_dental.head()
# -

# 3.c

print( 'The number of cases in demographic datasets is ' + str(final_demo_df.shape[0]))
print( 'The number of cases in dental datasets is ' + str(final_dental.shape[0]))
