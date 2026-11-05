# Week 7: the coin counter app (STARTER)
# Run with:  streamlit run app_starter.py
# Work through the TODO steps. app_final.py has the finished version.
import warnings
import numpy as np
import pandas as pd
import streamlit as st
from scipy import ndimage as ndi
from skimage import data, filters, measure, morphology, segmentation

warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(page_title="Coin counter", layout="wide")
st.title("The coin counter")
st.write("Move the sliders and watch the count change. There are 24 coins in this photo.")

coins = data.coins()
otsu = int(filters.threshold_otsu(coins))


def find_objects(img, threshold, radius, min_size, drop_border):
    mask = img > threshold
    if radius > 0:
        mask = morphology.opening(mask, morphology.disk(radius))
    if min_size > 0:
        mask = morphology.remove_small_objects(mask, min_size=min_size)
    mask = ndi.binary_fill_holes(mask)
    if drop_border:
        mask = segmentation.clear_border(mask)
    return mask, measure.label(mask)


# TODO step 1: show the photo with st.image(coins, caption="Original")

# TODO step 2: add sidebar controls
#   threshold = st.sidebar.slider("Threshold", 0, 255, otsu)
#   radius    = st.sidebar.slider("Opening radius", 0, 6, 2)
#   min_size  = st.sidebar.slider("Smallest object (pixels)", 0, 500, 100)
#   drop_border = st.sidebar.checkbox("Drop objects touching the border")

# TODO step 3: call find_objects(...) and show the mask in two columns
#   left, right = st.columns(2)
#   right.image((mask * 255).astype(np.uint8), caption="Mask")

# TODO step 4: build a table with measure.regionprops(labels), then
#   st.metric("Objects found", len(table))
#   st.dataframe(table)

# TODO step 5: tick the border checkbox. What is the count now?
