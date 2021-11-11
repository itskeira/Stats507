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

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency
import math
import scipy.stats as st
from scipy.stats import sem
from scipy.stats import norm
from statistics import mean
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from tabulate import tabulate

# +
#1.a

url1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT'
url2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT'
url3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT'
url4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'

cols = ['SEQN', 'RIDAGEYR', 'RIDRETH3','DMDEDUC2','DMDMARTL',
        'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR','RIAGENDR']

df1 = pd.read_sas(url1)
new_df1 = df1[cols].copy()
new_df1['cohort']='1'
final_df1 = new_df1.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'exam_status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight',
                            'gender',
                            'cohort'], axis=1, inplace=False)

df2 = pd.read_sas(url2)
new_df2 = df2[cols].copy()
new_df2['cohort']='2'
final_df2 = new_df2.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'exam_status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight',
                            'gender',
                            'cohort'], axis=1, inplace=False)

df3 = pd.read_sas(url3)
new_df3 = df3[cols].copy()
new_df3['cohort']='3'
final_df3 = new_df3.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'exam_status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight',
                            'gender',
                            'cohort'], axis=1, inplace=False)

df4 = pd.read_sas(url4)
new_df4 = df4[cols].copy()
new_df4['cohort']='4'
final_df4 = new_df4.set_axis(['id', 'age', 'race/ethnicity', 'education', 
                            'marital status', 'exam_status', 
                            'masked variance pseudo-psu', 
                            'masked variance pseudo-stratum', 
                            '2 year mec exam weight', 
                            '2 year interview weight',
                            'gender',
                            'cohort'], axis=1, inplace=False)


convert_dict = {'id': int,
                'age': int,
                'race/ethnicity': 'category',
                'education': 'category',
                'marital status': 'category',
                'exam_status': 'category',
                'masked variance pseudo-psu': int,
                'masked variance pseudo-stratum': int,
                '2 year mec exam weight': float,
                '2 year interview weight':float,
                'gender': 'category',
                'cohort': int
               }

all_df = [final_df1, final_df2, final_df3, final_df4]
demo_df = pd.concat(all_df,axis=0)
demo_df = demo_df.astype(convert_dict)

# check column types
print(demo_df.dtypes)

# save to pickle format
demo_df.to_pickle("./df.pkl")

# read pickle format file 
pkl_demo = pd.read_pickle("./df.pkl")
pkl_demo.head()

# +
#1.b

url_d1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT'
url_d2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT'
url_d3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT'
url_d4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT'

# cohort 1

dd1 = pd.read_sas(url_d1)
dental_col1 = ['SEQN', 'OHDDESTS']
dental_df1 = dd1[dental_col1].copy()

dental_col1[0] = 'id'
dental_col1[1] = 'ohx_status'
den1 = dental_df1.set_axis(dental_col1, axis=1, inplace=False)

# cohort 2
dd2 = pd.read_sas(url_d2)
dental_col2 = ['SEQN', 'OHDDESTS']
dental_df2 = dd2[dental_col2].copy()

dental_col2[0] = 'id'
dental_col2[1] = 'ohx_status'
den2 = dental_df2.set_axis(dental_col2, axis=1, inplace=False)

# cohort 3

dd3 = pd.read_sas(url_d3)
dental_col3 = ['SEQN', 'OHDDESTS']
dental_df3 = dd3[dental_col3].copy()

dental_col3[0] = 'id'
dental_col3[1] = 'ohx_status'
den3 = dental_df3.set_axis(dental_col3, axis=1, inplace=False)

# cohort 4

dd4 = pd.read_sas(url_d4)
dental_col4 = ['SEQN', 'OHDDESTS']
dental_df4 = dd4[dental_col4].copy()

dental_col4[0] = 'id'
dental_col4[1] = 'ohx_status'
den4 = dental_df4.set_axis(dental_col4, axis=1, inplace=False)

# combine
dental_df = [den1, den2, den3, den4]
final_dental = pd.concat(dental_df,axis=0)
final_dental['ohx_status'] = final_dental['ohx_status'] .astype('category')
final_dental['id'] = final_dental['id'].astype(int)

# check column types
print(final_dental.dtypes)

merged_df = pd.merge(demo_df,final_dental,how='left', left_on='id',right_on='id')

merged_df.head(3)

merged_df['under_20'] = [True if x < 20 else False for x in merged_df['age']]

condition = [(merged_df['education'] == 4) | (merged_df['education'] == 5), 
             (merged_df['under_20'] == True)|
             ((merged_df['education'] != 4)|(merged_df['education'] != 5))]
answer = ['some college/college graduate', 'No college/<20']
merged_df['college'] = np.select(condition, answer)

condition2 = [(merged_df['exam_status'] == 2) & (merged_df['ohx_status'] == 1), 
              (merged_df['ohx_status'] != 1)]
answer2 = ['complete', 'missing']
merged_df['ohx'] = np.select(condition2, answer2)

cols = ['id', 'gender', 'age', 'under_20', 'college', 'exam_status','ohx_status','ohx']
new_df = merged_df[cols]
new_df.head(5)

# +
#1.c

c_df = new_df.drop(new_df[new_df.exam_status != 2].index)
c_df.head()

num = len(new_df[new_df.exam_status != 2])
print('The number of subjects removed : ' + str(num))
print('The number of subjects remaining : ' + str(c_df.shape[0]))


# +
#1.d

under_tb = pd.crosstab(c_df['under_20'],c_df['ohx'])
under_tb.index = ['20 or older','under 20']

gender_tb = pd.crosstab(c_df['gender'],c_df['ohx'])
gender_tb.index = ['male', 'female']

col_tb = pd.crosstab(c_df['college'],c_df['ohx'])

tb = pd.concat([under_tb, gender_tb, col_tb], axis=0)
tb2 = tb.apply(lambda r: r/r.sum(), axis=1)

tuples = [('age (mean/se)',''),
         ('age < 20','20 or older'),
         ('age < 20', 'under 20'),
         ('gender', 'male'),
         ('gender','female'),
         ('college','no college/<20'),
         ('college', 'some college/college graduate')]

age_c = c_df[c_df.ohx == 'complete'].age.mean()
age_m = c_df[c_df.ohx == 'missing'].age.mean()
age_cd = stats.tstd(c_df[c_df.ohx == 'complete'].age)
age_md = stats.tstd(c_df[c_df.ohx == 'missing'].age)


f_format = "{0:.0f}({1:.4}%)"
f_format2 = "{0:.3f}({1:.4})"        

age0 = f_format2.format(age_c,age_cd)
age1 = f_format2.format(age_m,age_md)
          
x0 = f_format.format(tb.iloc[0, 0],tb2.iloc[0, 0]*100)
x1 = f_format.format(tb.iloc[1, 0],tb2.iloc[1, 0]*100)
x2 = f_format.format(tb.iloc[2, 0],tb2.iloc[2, 0]*100)
x3 = f_format.format(tb.iloc[3, 0],tb2.iloc[3, 0]*100)
x4 = f_format.format(tb.iloc[4, 0],tb2.iloc[4, 0]*100)
x5 = f_format.format(tb.iloc[5, 0],tb2.iloc[5, 0]*100)

y0 = f_format.format(tb.iloc[0, 1],tb2.iloc[0, 1]*100)
y1 = f_format.format(tb.iloc[1, 1],tb2.iloc[1, 1]*100)
y2 = f_format.format(tb.iloc[2, 1],tb2.iloc[2, 1]*100)
y3 = f_format.format(tb.iloc[3, 1],tb2.iloc[3, 1]*100)
y4 = f_format.format(tb.iloc[4, 1],tb2.iloc[4, 1]*100)
y5 = f_format.format(tb.iloc[5, 1],tb2.iloc[5, 1]*100)

index = pd.MultiIndex.from_tuples(tuples, names = ['variable name', 'level'])
tb3 = pd.DataFrame({'complete':[age0,x0, x1, x2, x3, x4, x5],
                  'missing': [age1,y0, y1, y2, y3, y4, y5]},
                  index=index)

# t-test
age_p = stats.ttest_ind(c_df[c_df.ohx == 'complete'].age,c_df[c_df.ohx == 'missing'].age)[1]
# Chi-square test of independence. 
p1= chi2_contingency(under_tb)[1]
p2 = chi2_contingency(gender_tb)[1]
p3 = chi2_contingency(col_tb)[1]

tb3['p-value'] = [age_p,p1,'-',p2,'-',p3,'-']

tb3
