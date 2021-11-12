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

# # Title
# *Stats 507, Fall 2021*
#
# Han Qiu
# November 11
# itskeira@umich.edu

# ## Filling missing values: Pandas.fillna() method
#   - Within pandas, a missing value is denoted by NaN/NA .
#   - It is very common to find several entries labelled NaN/NA by Python, when dealing with large dataset. 
#   - The `.fillna()`method helps to replace NaN/Na value in a Dataframe or Series with non-null data in a couple of ways.
#     

# ## Pandas.fillna() method
#   - Replace NA/NaN with a scalar value(e.g. 0).
#   - For example, you can set the value equals to 0 to fill holes using `value = 0`

import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
df

df.fillna(0)

# ## Pandas.fillna() method
#   - We can propagate non-NA/ non-NaN values forward or backward by using the `method` keyword.
#   - There are total four methods avaliable `backfill`, `bfill`, `pad`, `ffill`, where the first two fill values forward and last two fill values backward.
#   
#

df.fillna(method="ffill")

# ## Pandas.fillna() method
#   - If we only want consecutive gaps filled up to a certain number of data points, we can use the `limit` keyword.
#   - For example, we can only replace the first NaN element.

values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values)

df.fillna(value=values, limit=1)


