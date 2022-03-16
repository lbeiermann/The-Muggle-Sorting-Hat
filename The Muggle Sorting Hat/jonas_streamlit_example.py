#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:25:44 2022

@author: jonasschroeder

Streamlit example

"""
import pandas as pd
import streamlit as st


#-----------
# just a simple clustering and 2d scatter plot
#
# Author: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)
y_pred = KMeans(n_clusters=5, random_state=random_state).fit_predict(X)

# display title
st.title("The Muggle Sorting Head App")

# display text
st.text("This app will help teachers to sort their students into diverse groups")

# upload file
st.file_uploader("Upload student data")

# input: number of groups
st.number_input("How many groups would you like to form?")

# button
st.button('Start grouping')

# show data
local_path_jonas = "/Users/jonasschroeder/Desktop/GitHub Repo/The-Muggle-Sorting-Hat/"
df1 = pd.read_csv(local_path_jonas+"The Muggle Sorting Hat DataSet.csv")
df1["Gender"] = df1["Gender"].str.replace(" ", "")
df1["District"] = df1["District"].str.replace(" ", "")
df1["Name"] = df1["Name"].str.replace(" ", "")
df1["Friend 1"] = df1["Friend 1"].str.replace(" ", "")
df1["Friend 2 "] = df1["Friend 2 "].str.replace(" ", "")
df1.rename(columns = {"Friend 2 ":"Friend 2"}, inplace = True)
st.dataframe(df1)

# scatter plot 
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1,1,1)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Random Plot Title")


# show plot in app
st.pyplot(fig)
st.write(fig)

# copy this to your terminal after adapting it to your folder structure
# cd Desktop/GitHub\ Repo/The-Muggle-Sorting-Hat/
# streamlit run jonas_streamlit_example.py
