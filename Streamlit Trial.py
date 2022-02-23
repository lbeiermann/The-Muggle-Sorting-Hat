import pandas as pd
import streamlit as st

import numpy as np
import matplotlib.pyplot as plt
import requests

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from streamlit_lottie import st_lottie

intro = st.beta_container()
input = st.beta_container()
result = st.beta_container()

#animation setup
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r

#load animation
lottie_coding = load_lottieurl("")

#intro section
with intro:

st.title ("The Muggle Sorting App")
st. text ("Helping teachers to sort their students into classes clicks away")

#user input
with input:

st.file_uploader("Upload student data")
st.slider("How many class you would like to form?", min_value= 0, max_value=100, value= 20, steps=1)
st.button("Form Class")






