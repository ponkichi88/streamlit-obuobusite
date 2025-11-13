import streamlit as st
import datetime

st.set_page_config(
    page_title="愛の掲示板",
    layout="wide"
)

st.title('💬 お文具さんへの愛を叫ぼう！')
st.markdown('お文具さんと仲間たちへの愛や感謝のメッセージを自由に投稿してください。')

# 1. セッションステートの初期化
# 'comments'というキーがセッションステートに存在しない場合、空のリストで初期化する
if 'comments' not in st.session_state:
    st.session_state.comments = []

# 2. コメント投稿フォーム
with st.form("comment_form", clear_on_submit=True):
    # ユーザー名とメッセージの入力
    name = st.text_input('あなたの名前（任意）', value='名も無きファン')
    message = st.text_area('愛のメッセージ', placeholder='お文具さん、いつもありがとう！')
    
    # 送信ボタン
    submitted = st.form_submit_button("メッセージを投稿！")

    if submitted and message:
        # 新しいコメントを作成
        new_comment = {
            "name": name,
            "message": message,
            "time": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        }
        
        # コメントをリストの先頭に追加 (新しいものが上に来るように)
        st.session_state.comments.insert(0, new_comment)
        st.success('メッセージが投稿されました！')
    elif submitted and not message:
        st.error('メッセージを入力してください！')

st.header("💌 みんなの愛のメッセージ")

# 3. 投稿されたコメントの表示
if st.session_state.comments:
    # 最新の50件のみ表示（長くなりすぎるのを防ぐため）
    display_comments = st.session_state.comments[:50]
    
    for comment in display_comments:
        # メッセージを囲むコンテナ（ボックス）
        with st.container(border=True):
            st.markdown(f'**{comment["message"]}**')
            st.caption(f'投稿者: {comment["name"]} | 投稿時間: {comment["time"]}')
            
else:
    st.info("まだ誰もメッセージを投稿していません。一番乗りで愛を叫びましょう！")