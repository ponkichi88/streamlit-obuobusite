import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="フォトタイルメーカー",
    layout="wide"
)

st.title('🎨 フォトタイルメーカー')
st.markdown('あなたの写真で、世界に一つだけのモザイクアートを作りましょう！')

# サイドバーにナビゲーションを設定
with st.sidebar:
    st.header("🏠 アプリメニュー")
    st.markdown("---")

    st.page_link("main.py", label="ホーム", icon="🏠")
    st.page_link("pages/1_Upload_Tiles.py", label="タイル画像を投稿", icon="🖼️")
    st.page_link("pages/2_Create_Mosaic.py", label="モザイクアートを作成", icon="🧩")
    
    st.markdown("---")
    st.info("まずは「タイル画像を投稿」ページから、モザイクの素材となる写真をアップロードしてください。")

st.header('使い方')
st.markdown('''
1.  **タイル画像を投稿ページ**で、モザイクアートの素材となる写真を複数枚アップロードします。
2.  **モザイクアートを作成ページ**で、モザイク化したい元の画像を1枚アップロードします。
3.  アップロードしたタイル画像を使って、モザイクアートが生成されます！
''')