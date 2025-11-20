import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO

# サイドバーに表示する場合 (例: pages/1_Upload_Tiles.py のコードのどこかに追加)
with st.sidebar:
    st.header("ページ移動")
    st.page_link("pages/1_Upload_Tiles.py", label="🖼️ タイル画像を投稿", icon=None) 
    st.page_link("pages/2_Create_Mosaic.py", label="🧩 モザイクアートを作成", icon=None) 
    st.page_link("Home.py", label="🏠 ホームに戻る", icon=None)

st.set_page_config(
    page_title="タイル画像を投稿",
    layout="centered"
)

st.title('🖼️ タイル画像を投稿')
st.markdown('モザイクアートの素材となる写真を複数枚アップロードしてください。')
st.info('アップロードされた画像は、このセッション中のみ保存されます。アプリを閉じるとリセットされます。')

# セッションステートにタイル画像を保存するためのリストを初期化
if 'uploaded_tiles_data' not in st.session_state:
    st.session_state.uploaded_tiles_data = []

# 画像アップロードウィジェット
uploaded_files = st.file_uploader(
    "タイルとして使いたい画像を複数選択 (JPG, PNG)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    # 新しくアップロードされたファイルを処理
    new_tiles = []
    for uploaded_file in uploaded_files:
        # ファイルの内容をバイト列として読み込み、PIL Imageとして開く
        bytes_data = uploaded_file.getvalue()
        img = Image.open(BytesIO(bytes_data)).convert("RGB")
        
        # モザイクアートの効率化のため、タイル画像をリサイズして保存
        # ここでは例として16x16ピクセルに統一
        resized_img = img.resize((16, 16)) 
        
        # リサイズされた画像をバイト列に戻して保存
        buffered = BytesIO()
        resized_img.save(buffered, format="PNG")
        new_tiles.append(buffered.getvalue())
        
    # 重複を避けるため、既存のタイルに新しいタイルを追加
    # (より厳密な重複チェックは必要に応じて実装)
    current_tile_hashes = [hash(t) for t in st.session_state.uploaded_tiles_data]
    for tile_data in new_tiles:
        if hash(tile_data) not in current_tile_hashes:
            st.session_state.uploaded_tiles_data.append(tile_data)
            
    st.success(f"{len(uploaded_files)}枚の画像をタイルとしてアップロードしました！")

# 現在アップロードされているタイル画像を表示
if st.session_state.uploaded_tiles_data:
    st.subheader(f"現在アップロードされているタイル画像 ({len(st.session_state.uploaded_tiles_data)}枚)")
    
    # ギャラリー形式でタイル画像を表示
    cols = st.columns(6) # 1行に6枚表示
    for i, tile_data in enumerate(st.session_state.uploaded_tiles_data):
        with cols[i % 6]:
            st.image(tile_data, width=80) # 小さく表示
else:
    st.info("まだタイル画像がアップロードされていません。")

st.markdown("---")
st.write("タイル画像をアップロードしたら、「モザイクアートを作成」ページに進んでください。")