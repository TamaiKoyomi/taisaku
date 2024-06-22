import streamlit as st
import pandas as pd
import numpy as np

st.title('期末テスト対策問題')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("期末1-1.xlsx")

words_df = load_data()

st.write('家庭科、保健、歴史総合、生物の4教科をランダムで出題します。問題文が変だったらすみません。')

if st.button('問題を見る'):
    rarity_probs = {
        '家庭科': 0.1,
        '保健': 0.1,
        '歴史総合': 0.1,
        '生物': 0.1
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))

    subset_df = words_df[words_df['教科'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"教科: {st.session_state.selected_word['教科']}")
    st.write(f"問題: {st.session_state.selected_word['問題']}")

    # 意味を確認するボタンを追加
    if st.button('答えを確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"答え: {st.session_state.selected_word['解答']}")