import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv("metadata.csv")
df = df.dropna(subset=["title", "publish_time"]).copy()
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Interactive year range
year_range = st.slider("Select year range", int(df["year"].min()), int(df["year"].max()), (2020, 2021))
subset = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications per year
st.subheader("Publications by Year")
year_counts = subset["year"].value_counts().sort_index()
st.bar_chart(year_counts)

# Top journals
st.subheader("Top Journals")
top_journals = subset["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# Show sample data
st.subheader("Sample Data")
st.write(subset.head())

import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Function to clean and extract words
def get_title_words(titles):
    words = []
    for t in titles.dropna():
        words.extend(re.findall(r"\b\w+\b", t.lower()))
    return words

# Example: assuming you already have df loaded
title_words = get_title_words(df["title"])

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(title_words))

# Plot with matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
ax.set_title("Word Cloud of Paper Titles")

# Display in Streamlit
st.subheader("Word Cloud of Titles")
st.pyplot(fig)

