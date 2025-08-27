import streamlit as st
import pickle
import pandas as pd
import numpy as np
import random

# Load saved data
new_df = pickle.load(open('musicrec.pkl', 'rb'))
similarity = pickle.load(open('similarities.pkl', 'rb'))

# Ensure similarity is a NumPy array
if isinstance(similarity, pd.DataFrame):
    similarity = similarity.values

# Auto-detect title column
def get_title_column(df):
    for col in df.columns:
        if col.strip().lower() in ['title', 'song-name']:
            return col
    return None

# Add default posters if missing
if 'Poster' not in new_df.columns:
    poster_urls = [
        "https://picsum.photos/200?random=1",
        "https://picsum.photos/200?random=2",
        "https://picsum.photos/200?random=3",
        "https://picsum.photos/200?random=4",
        "https://picsum.photos/200?random=5"
    ]
    new_df['Poster'] = [random.choice(poster_urls) for _ in range(len(new_df))]

# ------------------------
# Recommendation Function
# ------------------------
def recommend(song_name):
    song_name = song_name.lower().strip()
    title_col = get_title_column(new_df)

    if not title_col:
        st.error("❌ Could not find a valid song title column.")
        return [], []

    match = new_df[new_df[title_col].str.lower() == song_name]

    if match.empty:
        return [], []

    index = match.index[0]
    distances = similarity[index]

    # ✅ Return 100 recommendations (excluding itself)
    music_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )
    music_list = [m for m in music_list if m[0] != index][:100]

    titles = []
    posters = []

    for i in music_list:
        title = new_df.iloc[i[0]][title_col]
        poster = new_df.iloc[i[0]].Poster
        titles.append(title)
        posters.append(poster)

    return titles, posters

# ------------------------
# Streamlit UI
# ------------------------

st.set_page_config(page_title="🎵 Music Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎶 Music Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a song name to get 100 similar song recommendations with album images.</p>", unsafe_allow_html=True)

song_input = st.text_input("🎧 Enter a song name:")

if st.button("Recommend"):
    if song_input.strip() == "":
        st.warning("⚠️ Please enter a song name.")
    else:
        titles, posters = recommend(song_input)

        if not titles:
            st.error("❌ Song not found. Try another name.")
        else:
            st.subheader(f"🎵 Top 100 Recommendations for **{song_input}**:")
            
            rows = [st.columns(5) for _ in range(20)]  # 20 rows × 5 columns = 100
            idx = 0
            for row in rows:
                for col in row:
                    if idx < len(titles):
                        with col:
                            st.image(posters[idx], width=150)
                            st.caption(titles[idx])
                            idx += 1
