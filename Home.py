import streamlit as st


# ページの基本設定（この設定は各ページで設定できます）
st.set_page_config(
    page_title="お文具さん推し活アプリ",
    layout="wide"  # 画面全体を使うワイドレイアウトに設定
)

with st.sidebar:
    st.header("🏠 ページナビゲーション")
    st.markdown("---") # 区切り線を追加

    st.page_link("Home.py", label="ホーム", icon="🏠")
    st.page_link("pages/1_Character_Intro.py", label="キャラクター情報", icon="1️⃣")

    st.page_link("pages/1_Mosaic_Art.py", label="モザイクアートメーカー", icon="🧩") # 🧩はパズルの絵文字
    st.markdown("---")

