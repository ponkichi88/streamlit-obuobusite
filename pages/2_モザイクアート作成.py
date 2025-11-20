import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO


col_links = st.columns(2) # リンクを2列に並べる

with col_links[0]:
    # 既存のリンクを移動
    st.page_link("pages/1_アップロード.py", label="🖼️ タイル画像を投稿", icon=None) 
    
with col_links[1]:
    # ホームへのリンクを配置
    st.page_link("ホーム.py", label="🏠 ホームに戻る", icon=None)
    
st.set_page_config(
    page_title="モザイクアートを作成",
    layout="wide"
)

st.title('🧩 モザイクアートを作成')
st.markdown('モザイク化したい画像をアップロードし、タイル画像を使ってモザイクアートを生成します。')



# --- (1) タイル画像の準備と平均色の計算 ---
# セッションステートからタイル画像を読み込む
if 'uploaded_tiles_data' not in st.session_state or not st.session_state.uploaded_tiles_data:
    st.warning("先に「タイル画像を投稿」ページでタイル画像をアップロードしてください。")
    st.stop() # タイル画像がなければ処理を停止

@st.cache_data(show_spinner="タイル画像データを準備中") # タイル画像が変更されない限りキャッシュ
def prepare_tiles(tiles_data):
    tiles = []
    avg_colors = []
    
    for data in tiles_data:
        tile = Image.open(BytesIO(data)).convert("RGB")
        # リサイズはアップロード時に済ませているはずだが、念のため
        tile = tile.resize((16, 16)) 
        tile_np = np.array(tile)
        avg_color = tile_np.mean(axis=(0, 1))
        
        tiles.append(tile)
        avg_colors.append(avg_color)
            
    return tiles, np.array(avg_colors)

# セッションステートからタイルデータを取得し、処理
tiles, avg_colors = prepare_tiles(st.session_state.uploaded_tiles_data)

# --- (2) 最も近いタイルを見つける関数 ---
def get_closest_tile(target_color, avg_colors_np, tiles):
    # ユークリッド距離 (色の差) を計算
    distances = np.sum((avg_colors_np - target_color) ** 2, axis=1)
    closest_index = np.argmin(distances)
    return tiles[closest_index]

# --- メインロジック ---

st.subheader("1. 元となる画像をアップロード")
uploaded_main_file = st.file_uploader("モザイクアートにしたい画像を1枚選択 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_main_file is not None:
    original_image = Image.open(uploaded_main_file).convert("RGB")
    
    MAX_SIZE = 2000
    w, h = original_image.size

    if max(w, h) > MAX_SIZE:
        ratio = MAX_SIZE / max(w, h)
        new_w = int(w * ratio)
        new_h = int(h * ratio)

        original_image = original_image.resize((new_w, new_h), Image.Resampling.LANCZOS)

        st.warning(f"処理速度を速めるため、元の画像を{new_w} × {new_h}に縮小しました。")
    
    st.subheader("アップロードされた元の画像")
    st.image(original_image, caption="元の画像", use_column_width=True)
    
    st.markdown("---")



    # --- サイドバーでの設定 ---
    with st.sidebar:
        st.header("モザイク設定")
        tile_size = 16 # タイル画像の固定サイズ
        
        # モザイクの粗さ (元画像を何分の1に縮小するか)
        # 値が大きいほどタイルが細かく見え、元の画像に近くなる
        reduction_factor = st.slider(
            "モザイクの粗さ (値が小さいほどタイルが細かく表示されます)",
            min_value=5,
            max_value=50,
            value=20,
            step=5
        )
        
        process_button = st.button("モザイクアートを生成開始", use_container_width=True)

    if process_button:
        with st.spinner('モザイクアートを生成中... 少々お待ちください...'):
            # 元画像を縮小 (処理速度のため、これがモザイクの「設計図」となる)
            w, h = original_image.size
            new_w = w // reduction_factor
            new_h = h // reduction_factor
            
            # 縮小画像にタイルが敷き詰められる
            resized_img = original_image.resize((new_w, new_h))
            resized_np = np.array(resized_img)
            
            # モザイクアートの最終サイズ (タイルサイズ * 設計図のサイズ)
            final_w = new_w * tile_size
            final_h = new_h * tile_size
            
            mosaic_art = Image.new('RGB', (final_w, final_h))

            # 設計図の各ピクセルに対して、最も近い色のタイルを貼り付ける
            for y in range(new_h):
                for x in range(new_w):
                    target_color = resized_np[y, x]
                    closest_tile = get_closest_tile(target_color, avg_colors, tiles)
                    
                    mosaic_art.paste(
                        closest_tile, 
                        (x * tile_size, y * tile_size)
                    )

            # 最終結果の表示
            st.subheader("完成したモザイクアート")
            st.image(mosaic_art, caption="あなただけのモザイクアート！", use_column_width=True)
            
            # ダウンロードボタン
            buf = BytesIO()
            mosaic_art.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="モザイクアートをダウンロード (PNG)",
                data=byte_im,
                file_name="my_photo_mosaic_art.png",
                mime="image/png"
            )
else:
    st.info('モザイク化したい画像をアップロードしてください。')

