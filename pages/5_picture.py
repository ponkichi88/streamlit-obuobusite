import streamlit as st

st.set_page_config(
    page_title="お文具さんイラスト集",
    layout="wide"
)

st.title('🎨 お文具さんといっしょ イラストギャラリー')
st.markdown('お文具さんと仲間たちの素敵なイラストを紹介します。')

st.markdown("---")

# ----------------------------------------------------
# 画像ファイルの表示（ローカルファイルを使用する場合）
# ----------------------------------------------------

# 例 1: プリンと一緒のイラスト
st.subheader("🍮 仲良しプリンと")
col1, col2 = st.columns(2)

with col1:
    # ローカルの画像ファイルを指定 (アプリと同じディレクトリにあると仮定)
    # 実際には、画像ファイル名を正しいものに置き換えてください
    st.image(
        'pages/E3Wun3WVoAIDFLS.jpg', 
        caption='まったり午後のプリンタイム', 
        width=300
    )

with col2:
    # 例 2: みんな集合のイラスト
    st.subheader("🎉 みんなでワイワイ")
    st.image(
        'pages/ogp.png', 
        caption='全員集合！楽しそうな日常の風景', 
        use_column_width='always' # カラムの幅いっぱいに表示
    )

st.markdown("---")
