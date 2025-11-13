import streamlit as st

# ページの基本設定（この設定は各ページで設定できます）
st.set_page_config(
    page_title="お文具さん推し活アプリ",
    layout="wide"  # 画面全体を使うワイドレイアウトに設定
)

st.title('お文具さんといっしょ 推し活部屋')
st.markdown('ようこそ、お文具さんとみんなの世界へ！')


st.info('左側のサイドバーから、各ページに移動できます。')

st.header('お知らせ')
st.success('お文具さんといっしょのゲームが発売！')