import streamlit as st

st.set_page_config(
    page_title="SNSリンク集",
    layout="wide"
)

st.title('🔗 お文具さん SNSリンク集')
st.markdown('お文具さんといっしょの公式情報や、最新情報をチェックしましょう！')
st.info('アイコンをクリックすると、各プラットフォームに移動します。')

# ----------------------------------------------------
# 1. リンク集の作成
# ----------------------------------------------------

# Google検索で得られたお文具さん関連の公式SNSリンクを仮定して作成しています
sns_links = [
    {"name": "YouTube (メインチャンネル)", "url": "https://youtube.com/@imoko_iimo?si=mPY5nojyS0neujYC", "icon": "▶️", "color": "#FF0000"},
    {"name": "X (旧 Twitter) 公式アカウント", "url": "https://x.com/imoko_iimo?s=20", "icon": "🐦", "color": "#1DA1F2"},
    {"name": "Instagram 公式アカウント", "url": "https://www.instagram.com/obungu_mofumofu?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==", "icon": "📸", "color": "#C13584"},
    # 必要に応じて他のリンクを追加
    {"name": "公式ウェブサイト/ブログ", "url": "https://obungu-official.jp/", "icon": "🌐", "color": "#28B463"},
]

st.header('公式リンクぷ')
cols = st.columns(len(sns_links)) # リンクの数だけカラムを作成

for i, link in enumerate(sns_links):
    # CSSでボタンに色を付け、リンクを埋め込む
    button_html = f"""
    <a href="{link['url']}" target="_blank" style="text-decoration: none;">
        <button style="
            background-color: {link['color']};
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        ">
            {link['icon']} {link['name']}
        </button>
    </a>
    """
    with cols[i]:
        st.markdown(button_html, unsafe_allow_html=True)
        
st.markdown("---")

# ----------------------------------------------------
# 2. YouTube埋め込みコンテンツの作成
# ----------------------------------------------------

st.header('🎥 最新のYouTube動画をチェック')

# ここに、埋め込みたい動画のURLを貼り付けます
# 例: https://www.youtube.com/watch?v=xxxxxxxxxxx
youtube_url = "YOUR_SPECIFIC_YOUTUBE_VIDEO_URL_HERE" 

if youtube_url != "YOUR_SPECIFIC_YOUTUBE_VIDEO_URL_HERE":
    # Streamlitの st.video() を使用して、YouTube動画を埋め込み
    st.video(youtube_url)
    st.caption('この動画を埋め込んでいます。')
else:
    st.warning('動画のURLが設定されていません。`st.video()`にYouTubeのURLを貼り付けてください。')


# ----------------------------------------------------
# 3. X (旧Twitter) の埋め込み（タイムラインや特定のポスト）
# ----------------------------------------------------

st.header('🐦 X (旧 Twitter) 埋め込み')
st.info('StreamlitにはXの埋め込み専用関数がないため、カスタムHTMLを使います。')

# Xの埋め込みコードの例（特定の投稿やタイムラインのウィジェットコードをここに貼り付ける）
# Xの埋め込みは、公式のウィジェット作成ツールで生成したHTMLコードを使用するのが最も確実です。
x_embed_html = """
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">お文具さんにプリンをあげたい<br>🍮🍮🍮🍮🍮</p>&mdash; お文具＠書籍発売中🍮 (@obungu_san) <a href="https://twitter.com/obungu_san/status/1234567890123456789?ref_src=twsrc%5Etfw">日付</a></blockquote> 
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
"""

# HTMLを直接埋め込むために st.components.v1.html を使用（より安全ですが、今回はシンプルな st.markdown で）
st.markdown(x_embed_html, unsafe_allow_html=True)