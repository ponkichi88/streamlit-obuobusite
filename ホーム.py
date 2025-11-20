import streamlit as st

# ページの基本設定
st.set_page_config(
    page_title="ホーム",
    layout="wide"
)

st.title('🎨 フォトタイルメーカー')
st.markdown('あなたの写真で、世界に一つだけのモザイクアートを作りましょう！')

st.subheader("🚀 クイックスタート")

col_links = st.columns(3) # リンクを3列に並べる

with col_links[0]:
    # 既存のリンクを移動
    st.page_link("pages/1_アップロード.py", label="🖼️ タイル画像を投稿", icon=None) 

with col_links[1]:
    # 既存のリンクを移動
    st.page_link("pages/2_モザイクアート作成.py", label="🧩 モザイクアートを作成", icon=None) 
    
with col_links[2]:
    # ホームへのリンクを配置
    st.page_link("ホーム.py", label="🏠 ホームに戻る", icon=None)

st.header('使い方')
st.markdown('''
1.  **タイル画像を投稿ページ**で、モザイクアートの素材となる写真を複数枚アップロードします。
2.  **モザイクアートを作成ページ**で、モザイク化したい元の画像を1枚アップロードします。
3.  アップロードしたタイル画像を使って、モザイクアートが生成されます！
''')



# サイドバーにナビゲーションを設定
with st.sidebar:
    st.header("🏠 アプリメニュー")
    st.markdown("---")

    st.info("左側のボタンをクリックしてページを移動してください。")
    st.markdown("---")

    st.info("まずは「タイル画像を投稿」ページから、モザイクの素材となる写真をアップロードしてください。")