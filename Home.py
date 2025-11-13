import streamlit as st


# ページの基本設定（この設定は各ページで設定できます）
st.set_page_config(
    page_title="お文具さん推し活アプリ",
    layout="wide"  # 画面全体を使うワイドレイアウトに設定
)

st.title('お文具さんといっしょ 推し活部屋')
st.markdown('ようこそ、お文具さんとみんなの世界へ！')


st.info('左側のサイドバーから、各ページに移動できます。')

with st.sidebar:
    st.header("🏠 ページナビゲーション")
    st.markdown("---") # 区切り線を追加

    st.page_link("Home.py", label="ホーム", icon="🏠")
    st.page_link("pages/1_Character_Intro.py", label="キャラクター情報", icon="1️⃣")
    
    # 2ページ目のファイル名が「2_Oshikatsu_Diary.py」で正しいか確認
    st.page_link("pages/2_Oshikatsu_Diary.py", label="お文具さんたちへの愛の言葉掲示板", icon="2️⃣", disabled=True)
    
    st.page_link("pages/3_SNS.py", label="SNSリンク集", icon="🌎")
    st.markdown("---")


st.header('お知らせ')
st.success('お文具さんといっしょのゲームが発売！')